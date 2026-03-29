#!/usr/bin/env python3
"""
PDF 提取图片工具
使用 PyMuPDF (fitz) 从 PDF 中提取嵌入的图片
"""

import sys
import argparse
import os
import fitz  # PyMuPDF


def extract_images(input_path, output_dir, min_width=100, min_height=100, image_format="png"):
    """
    从 PDF 中提取所有图片
    
    Args:
        input_path: 输入 PDF 路径
        output_dir: 输出目录
        min_width: 最小图片宽度（过滤小图片）
        min_height: 最小图片高度（过滤小图片）
        image_format: 输出图片格式 (png, jpg, jpeg)
    
    Returns:
        tuple: (成功数量, 总数量, 保存路径列表)
    """
    try:
        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)
        
        doc = fitz.open(input_path)
        image_list = []
        saved_paths = []
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            image_list.extend(page.get_images())
        
        # 去重
        image_list = list(set(image_list))
        
        success_count = 0
        for img_index, img in enumerate(image_list, 1):
            xref = img[0]
            
            # 提取图片
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # 获取图片尺寸
            pix = fitz.Pixmap(doc, xref)
            width = pix.width
            height = pix.height
            
            # 过滤小图片
            if width < min_width or height < min_height:
                continue
            
            # 确定输出格式
            if image_format.lower() in ["jpg", "jpeg"]:
                output_ext = "jpg"
                if pix.n >= 5:  # CMYK 或其他特殊色彩空间
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                img_data = pix.tobytes("jpeg")
            else:
                output_ext = "png"
                img_data = pix.tobytes("png")
            
            # 保存图片
            output_filename = f"image_{img_index:03d}.{output_ext}"
            output_path = os.path.join(output_dir, output_filename)
            
            with open(output_path, "wb") as f:
                f.write(img_data)
            
            saved_paths.append(output_path)
            success_count += 1
            
            print(f"  提取图片 {img_index}: {width}x{height} -> {output_filename}")
        
        doc.close()
        return success_count, len(image_list), saved_paths
        
    except Exception as e:
        print(f"提取图片失败: {e}", file=sys.stderr)
        return 0, 0, []


def extract_images_by_page(input_path, output_dir, pages=None, min_width=100, min_height=100, image_format="png"):
    """
    按页面提取图片
    
    Args:
        input_path: 输入 PDF 路径
        output_dir: 输出目录
        pages: 页码列表（None 表示所有页）
        min_width: 最小图片宽度
        min_height: 最小图片高度
        image_format: 输出图片格式
    
    Returns:
        dict: 页码 -> 图片路径列表
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        doc = fitz.open(input_path)
        result = {}
        
        for page_num in range(len(doc)):
            # 如果指定了页码，只处理指定页
            if pages is not None and page_num not in pages:
                continue
            
            page = doc[page_num]
            images = page.get_images()
            
            if not images:
                continue
            
            page_images = []
            
            for img_index, img in enumerate(images, 1):
                xref = img[0]
                
                base_image = doc.extract_image(xref)
                pix = fitz.Pixmap(doc, xref)
                
                # 过滤小图片
                if pix.width < min_width or pix.height < min_height:
                    continue
                
                # 确定输出格式
                if image_format.lower() in ["jpg", "jpeg"]:
                    output_ext = "jpg"
                    if pix.n >= 5:
                        pix = fitz.Pixmap(fitz.csRGB, pix)
                    img_data = pix.tobytes("jpeg")
                else:
                    output_ext = "png"
                    img_data = pix.tobytes("png")
                
                # 保存图片
                output_filename = f"page{page_num + 1:03d}_img{img_index:02d}.{output_ext}"
                output_path = os.path.join(output_dir, output_filename)
                
                with open(output_path, "wb") as f:
                    f.write(img_data)
                
                page_images.append(output_path)
            
            if page_images:
                result[page_num + 1] = page_images
        
        doc.close()
        return result
        
    except Exception as e:
        print(f"提取图片失败: {e}", file=sys.stderr)
        return {}


def get_pdf_image_info(input_path):
    """
    获取 PDF 图片信息
    
    Args:
        input_path: PDF 路径
    
    Returns:
        list: 图片信息列表
    """
    try:
        doc = fitz.open(input_path)
        image_info = []
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            images = page.get_images()
            
            for img in images:
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                
                image_info.append({
                    "page": page_num + 1,
                    "xref": xref,
                    "width": pix.width,
                    "height": pix.height,
                    "colorspace": pix.colorspace.name if pix.colorspace else "unknown",
                })
        
        doc.close()
        return image_info
        
    except Exception as e:
        print(f"获取图片信息失败: {e}", file=sys.stderr)
        return []


def main():
    parser = argparse.ArgumentParser(
        description="PDF 提取图片工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 提取所有图片
  %(prog)s extract input.pdf ./images
  
  # 提取图片，最小尺寸 200x200
  %(prog)s extract input.pdf ./images --min-size 200
  
  # 提取图片为 JPG 格式
  %(prog)s extract input.pdf ./images --format jpg
  
  # 按页面提取图片
  %(prog)s by-page input.pdf ./images
  
  # 提取指定页面的图片
  %(prog)s by-page input.pdf ./images --pages 1,3,5
  
  # 查看图片信息
  %(prog)s info input.pdf
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="命令")
    
    # 提取所有图片命令
    extract_parser = subparsers.add_parser("extract", help="提取所有图片")
    extract_parser.add_argument("input", help="输入 PDF 文件")
    extract_parser.add_argument("output", help="输出目录")
    extract_parser.add_argument("--min-size", type=int, default=100, help="最小图片尺寸（默认: 100）")
    extract_parser.add_argument("--format", choices=["png", "jpg", "jpeg"], default="png", help="输出格式（默认: png）")
    
    # 按页面提取命令
    bypage_parser = subparsers.add_parser("by-page", help="按页面提取图片")
    bypage_parser.add_argument("input", help="输入 PDF 文件")
    bypage_parser.add_argument("output", help="输出目录")
    bypage_parser.add_argument("--pages", help="指定页码（如: 1,3,5-7）")
    bypage_parser.add_argument("--min-size", type=int, default=100, help="最小图片尺寸（默认: 100）")
    bypage_parser.add_argument("--format", choices=["png", "jpg", "jpeg"], default="png", help="输出格式（默认: png）")
    
    # 信息命令
    info_parser = subparsers.add_parser("info", help="查看图片信息")
    info_parser.add_argument("input", help="PDF 文件")
    
    args = parser.parse_args()
    
    # 解析页码
    def parse_pages(pages_str):
        if not pages_str:
            return None
        result = []
        for part in pages_str.split(","):
            if "-" in part:
                start, end = map(int, part.split("-"))
                result.extend(range(start - 1, end))
            else:
                result.append(int(part) - 1)
        return result
    
    if args.command == "extract":
        success, total, saved = extract_images(
            args.input,
            args.output,
            min_width=args.min_size,
            min_height=args.min_size,
            image_format=args.format
        )
        
        print(f"✅ 提取完成")
        print(f"   总图片数: {total}")
        print(f"   提取数量: {success}")
        print(f"   输出目录: {args.output}")
        
    elif args.command == "by-page":
        pages = parse_pages(args.pages)
        
        result = extract_images_by_page(
            args.input,
            args.output,
            pages=pages,
            min_width=args.min_size,
            min_height=args.min_size,
            image_format=args.format
        )
        
        print(f"✅ 提取完成")
        total = sum(len(imgs) for imgs in result.values())
        print(f"   总图片数: {total}")
        print(f"   输出目录: {args.output}")
        for page, imgs in result.items():
            print(f"   第 {page} 页: {len(imgs)} 张图片")
        
    elif args.command == "info":
        info = get_pdf_image_info(args.input)
        
        if not info:
            print("未找到图片")
        else:
            print(f"📄 PDF 图片信息:")
            print(f"   总图片数: {len(info)}")
            print()
            for img in info:
                print(f"   第 {img['page']} 页: {img['width']}x{img['height']} ({img['colorspace']})")
        
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
