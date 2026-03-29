#!/usr/bin/env python3
"""
PDF 水印工具
使用 PyMuPDF (fitz) 实现 PDF 添加水印
"""

import sys
import argparse
import fitz  # PyMuPDF


def add_text_watermark(input_path, output_path, text, 
                       fontsize=50, opacity=0.3, color=(0.8, 0.8, 0.8),
                       position="center", rotation=45, pages=None):
    """
    添加文字水印
    
    Args:
        input_path: 输入 PDF 路径
        output_path: 输出 PDF 路径
        text: 水印文字
        fontsize: 字体大小
        opacity: 透明度 (0-1)
        color: RGB 颜色元组 (0-1)
        position: 位置 (center, diagonal, top-left, top-right, bottom-left, bottom-right)
        rotation: 旋转角度
        pages: 页码列表 (None 表示所有页)
    
    Returns:
        bool: 是否成功
    """
    try:
        doc = fitz.open(input_path)
        
        for page_num in range(len(doc)):
            # 如果指定了页码，只处理指定页
            if pages is not None and page_num not in pages:
                continue
                
            page = doc[page_num]
            
            # 计算水印位置
            rect = page.rect
            center_x = rect.width / 2
            center_y = rect.height / 2
            
            # 创建水印文本
            text_length = fitz.get_text_length(text, fontsize=fontsize)
            
            # 根据位置设置坐标
            if position == "center":
                x, y = center_x, center_y
            elif position == "diagonal":
                x, y = center_x, center_y
            elif position == "top-left":
                x, y = rect.width * 0.2, rect.height * 0.2
            elif position == "top-right":
                x, y = rect.width * 0.8, rect.height * 0.2
            elif position == "bottom-left":
                x, y = rect.width * 0.2, rect.height * 0.8
            elif position == "bottom-right":
                x, y = rect.width * 0.8, rect.height * 0.8
            else:
                x, y = center_x, center_y
            
            # 添加水印
            page.insert_text(
                (x, y),
                text,
                fontsize=fontsize,
                color=color,
                rotate=rotation,
                overlay=True,
                render_mode=3,  # 透明模式
            )
            
            # 设置透明度
            # 注意：PyMuPDF 的透明度需要通过 shape 实现
            shape = page.new_shape()
            shape.insert_text(
                (x, y),
                text,
                fontsize=fontsize,
                color=color,
                rotate=rotation,
            )
            shape.commit(overlay=True)
        
        doc.save(output_path)
        doc.close()
        return True
        
    except Exception as e:
        print(f"添加水印失败: {e}", file=sys.stderr)
        return False


def add_image_watermark(input_path, output_path, image_path,
                        scale=0.5, opacity=0.3, position="center",
                        rotation=0, pages=None):
    """
    添加图片水印
    
    Args:
        input_path: 输入 PDF 路径
        output_path: 输出 PDF 路径
        image_path: 水印图片路径
        scale: 缩放比例
        opacity: 透明度 (0-1)
        position: 位置 (center, diagonal, top-left, top-right, bottom-left, bottom-right)
        rotation: 旋转角度
        pages: 页码列表 (None 表示所有页)
    
    Returns:
        bool: 是否成功
    """
    try:
        doc = fitz.open(input_path)
        
        # 加载图片
        img = fitz.open(image_path)
        img_page = img[0]
        img_rect = img_page.rect
        
        # 缩放图片
        img_rect *= scale
        
        for page_num in range(len(doc)):
            # 如果指定了页码，只处理指定页
            if pages is not None and page_num not in pages:
                continue
                
            page = doc[page_num]
            rect = page.rect
            
            # 计算水印位置
            center_x = rect.width / 2
            center_y = rect.height / 2
            
            # 根据位置设置坐标
            if position == "center":
                x = center_x - img_rect.width / 2
                y = center_y - img_rect.height / 2
            elif position == "top-left":
                x = rect.width * 0.1
                y = rect.height * 0.1
            elif position == "top-right":
                x = rect.width * 0.9 - img_rect.width
                y = rect.height * 0.1
            elif position == "bottom-left":
                x = rect.width * 0.1
                y = rect.height * 0.9 - img_rect.height
            elif position == "bottom-right":
                x = rect.width * 0.9 - img_rect.width
                y = rect.height * 0.9 - img_rect.height
            else:
                x = center_x - img_rect.width / 2
                y = center_y - img_rect.height / 2
            
            # 添加图片水印
            page.insert_image(
                fitz.Rect(x, y, x + img_rect.width, y + img_rect.height),
                filename=image_path,
                overlay=True,
                rotate=rotation,
            )
        
        doc.save(output_path)
        doc.close()
        img.close()
        return True
        
    except Exception as e:
        print(f"添加图片水印失败: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description="PDF 水印工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 添加文字水印（居中）
  %(prog)s text input.pdf output.pdf "机密文件"
  
  # 添加文字水印（斜角，透明度 0.5）
  %(prog)s text input.pdf output.pdf "机密文件" --opacity 0.5 --position diagonal
  
  # 添加文字水印（指定页码）
  %(prog)s text input.pdf output.pdf "机密文件" --pages 1,3,5
  
  # 添加图片水印
  %(prog)s image input.pdf output.pdf watermark.png --scale 0.3 --opacity 0.3
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="命令")
    
    # 文字水印命令
    text_parser = subparsers.add_parser("text", help="添加文字水印")
    text_parser.add_argument("input", help="输入 PDF 文件")
    text_parser.add_argument("output", help="输出 PDF 文件")
    text_parser.add_argument("text", help="水印文字")
    text_parser.add_argument("--fontsize", type=int, default=50, help="字体大小（默认: 50）")
    text_parser.add_argument("--opacity", type=float, default=0.3, help="透明度 0-1（默认: 0.3）")
    text_parser.add_argument("--color", default="0.8,0.8,0.8", help="RGB 颜色（默认: 0.8,0.8,0.8 浅灰色）")
    text_parser.add_argument("--position", choices=["center", "diagonal", "top-left", "top-right", "bottom-left", "bottom-right"],
                           default="center", help="水印位置（默认: center）")
    text_parser.add_argument("--rotation", type=int, default=45, help="旋转角度（默认: 45）")
    text_parser.add_argument("--pages", help="指定页码（如: 1,3,5-7）")
    
    # 图片水印命令
    image_parser = subparsers.add_parser("image", help="添加图片水印")
    image_parser.add_argument("input", help="输入 PDF 文件")
    image_parser.add_argument("output", help="输出 PDF 文件")
    image_parser.add_argument("image", help="水印图片文件")
    image_parser.add_argument("--scale", type=float, default=0.5, help="缩放比例（默认: 0.5）")
    image_parser.add_argument("--opacity", type=float, default=0.3, help="透明度 0-1（默认: 0.3）")
    image_parser.add_argument("--position", choices=["center", "top-left", "top-right", "bottom-left", "bottom-right"],
                            default="center", help="水印位置（默认: center）")
    image_parser.add_argument("--rotation", type=int, default=0, help="旋转角度（默认: 0）")
    image_parser.add_argument("--pages", help="指定页码（如: 1,3,5-7）")
    
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
    
    if args.command == "text":
        # 解析颜色
        color = tuple(map(float, args.color.split(",")))
        
        pages = parse_pages(args.pages)
        
        success = add_text_watermark(
            args.input, args.output, args.text,
            fontsize=args.fontsize,
            opacity=args.opacity,
            color=color,
            position=args.position,
            rotation=args.rotation,
            pages=pages
        )
        
        if success:
            print(f"✅ 添加文字水印成功: {args.output}")
            print(f"   水印文字: {args.text}")
            print(f"   字体大小: {args.fontsize}")
            print(f"   透明度: {args.opacity}")
        else:
            sys.exit(1)
            
    elif args.command == "image":
        pages = parse_pages(args.pages)
        
        success = add_image_watermark(
            args.input, args.output, args.image,
            scale=args.scale,
            opacity=args.opacity,
            position=args.position,
            rotation=args.rotation,
            pages=pages
        )
        
        if success:
            print(f"✅ 添加图片水印成功: {args.output}")
            print(f"   水印图片: {args.image}")
            print(f"   缩放比例: {args.scale}")
            print(f"   透明度: {args.opacity}")
        else:
            sys.exit(1)
            
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
