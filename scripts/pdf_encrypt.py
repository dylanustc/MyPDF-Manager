#!/usr/bin/env python3
"""
PDF 加密工具
使用 PyMuPDF (fitz) 实现 PDF 加密
"""

import sys
import argparse
import fitz  # PyMuPDF


def encrypt_pdf(input_path, output_path, user_password=None, owner_password=None, permissions=None):
    """
    加密 PDF 文件
    
    Args:
        input_path: 输入 PDF 路径
        output_path: 输出 PDF 路径
        user_password: 用户密码（打开 PDF 需要）
        owner_password: 所有者密码（修改权限需要）
        permissions: 权限字典，如 {'print': True, 'copy': False}
    
    Returns:
        bool: 是否成功
    """
    try:
        doc = fitz.open(input_path)
        
        # 默认权限：允许打印，禁止复制和修改
        if permissions is None:
            permissions = {
                fitz.PDF_PERM_PRINT: True,
                fitz.PDF_PERM_COPY: False,
                fitz.PDF_PERM_MODIFY: False,
                fitz.PDF_PERM_ANNOTATE: False,
                fitz.PDF_PERM_FILL_FORM: False,
                fitz.PDF_PERM_EXTRACT: False,
                fitz.PDF_PERM_ASSEMBLE: False,
            }
        
        # 加密保存
        # encryption 方法：PDF_ENCRYPT_AES_256（推荐），PDF_ENCRYPT_AES_128，PDF_ENCRYPT_RC4_128
        doc.save(
            output_path,
            encryption=fitz.PDF_ENCRYPT_AES_256,
            owner_pw=owner_password or "owner",
            user_pw=user_password,
            permissions=permissions
        )
        
        doc.close()
        return True
        
    except Exception as e:
        print(f"加密失败: {e}", file=sys.stderr)
        return False


def decrypt_pdf(input_path, output_path, password):
    """
    解密 PDF 文件
    
    Args:
        input_path: 输入加密 PDF 路径
        output_path: 输出解密 PDF 路径
        password: PDF 密码
    
    Returns:
        bool: 是否成功
    """
    try:
        doc = fitz.open(input_path)
        
        if doc.is_encrypted:
            if not doc.authenticate(password):
                print("密码错误或 PDF 未加密", file=sys.stderr)
                return False
        
        # 保存为无加密的 PDF
        doc.save(output_path)
        doc.close()
        return True
        
    except Exception as e:
        print(f"解密失败: {e}", file=sys.stderr)
        return False


def get_pdf_encryption_info(input_path):
    """
    获取 PDF 加密信息
    
    Args:
        input_path: PDF 路径
    
    Returns:
        dict: 加密信息
    """
    try:
        doc = fitz.open(input_path)
        
        if doc.is_encrypted:
            return {
                "encrypted": True,
                "method": "加密 PDF",
                "permissions": {
                    "print": doc.permissions & fitz.PDF_PERM_PRINT,
                    "copy": doc.permissions & fitz.PDF_PERM_COPY,
                    "modify": doc.permissions & fitz.PDF_PERM_MODIFY,
                    "annotate": doc.permissions & fitz.PDF_PERM_ANNOTATE,
                }
            }
        else:
            return {
                "encrypted": False,
                "method": None,
                "permissions": None
            }
            
    except Exception as e:
        return {
            "encrypted": None,
            "error": str(e)
        }
    finally:
        if 'doc' in locals():
            doc.close()


def main():
    parser = argparse.ArgumentParser(
        description="PDF 加密/解密工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 加密 PDF（设置用户密码）
  %(prog)s encrypt input.pdf output.pdf --user-password 123456
  
  # 加密 PDF（设置用户密码和所有者密码）
  %(prog)s encrypt input.pdf output.pdf --user-password 123456 --owner-password admin
  
  # 解密 PDF
  %(prog)s decrypt encrypted.pdf decrypted.pdf --password 123456
  
  # 查看 PDF 加密信息
  %(prog)s info input.pdf
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="命令")
    
    # 加密命令
    encrypt_parser = subparsers.add_parser("encrypt", help="加密 PDF")
    encrypt_parser.add_argument("input", help="输入 PDF 文件")
    encrypt_parser.add_argument("output", help="输出 PDF 文件")
    encrypt_parser.add_argument("--user-password", help="用户密码（打开 PDF 需要）")
    encrypt_parser.add_argument("--owner-password", default="owner", help="所有者密码（默认: owner）")
    encrypt_parser.add_argument("--allow-print", action="store_true", help="允许打印")
    encrypt_parser.add_argument("--allow-copy", action="store_true", help="允许复制")
    encrypt_parser.add_argument("--allow-modify", action="store_true", help="允许修改")
    
    # 解密命令
    decrypt_parser = subparsers.add_parser("decrypt", help="解密 PDF")
    decrypt_parser.add_argument("input", help="输入加密 PDF 文件")
    decrypt_parser.add_argument("output", help="输出解密 PDF 文件")
    decrypt_parser.add_argument("--password", required=True, help="PDF 密码")
    
    # 信息命令
    info_parser = subparsers.add_parser("info", help="查看 PDF 加密信息")
    info_parser.add_argument("input", help="PDF 文件")
    
    args = parser.parse_args()
    
    if args.command == "encrypt":
        if not args.user_password:
            print("错误: 加密需要设置 --user-password", file=sys.stderr)
            sys.exit(1)
        
        permissions = {
            fitz.PDF_PERM_PRINT: args.allow_print,
            fitz.PDF_PERM_COPY: args.allow_copy,
            fitz.PDF_PERM_MODIFY: args.allow_modify,
            fitz.PDF_PERM_ANNOTATE: args.allow_modify,
            fitz.PDF_PERM_FILL_FORM: args.allow_modify,
            fitz.PDF_PERM_EXTRACT: args.allow_copy,
            fitz.PDF_PERM_ASSEMBLE: args.allow_modify,
        }
        
        success = encrypt_pdf(
            args.input, 
            args.output, 
            args.user_password, 
            args.owner_password,
            permissions
        )
        
        if success:
            print(f"✅ 加密成功: {args.output}")
            print(f"   用户密码: {args.user_password}")
            print(f"   所有者密码: {args.owner_password}")
            print(f"   权限: 打印={'允许' if args.allow_print else '禁止'}, 复制={'允许' if args.allow_copy else '禁止'}, 修改={'允许' if args.allow_modify else '禁止'}")
        else:
            sys.exit(1)
            
    elif args.command == "decrypt":
        success = decrypt_pdf(args.input, args.output, args.password)
        
        if success:
            print(f"✅ 解密成功: {args.output}")
        else:
            sys.exit(1)
            
    elif args.command == "info":
        info = get_pdf_encryption_info(args.input)
        
        if info.get("error"):
            print(f"错误: {info['error']}", file=sys.stderr)
            sys.exit(1)
        
        if info["encrypted"]:
            print(f"📄 PDF 状态: 已加密")
            print(f"   权限:")
            print(f"   - 打印: {'允许' if info['permissions']['print'] else '禁止'}")
            print(f"   - 复制: {'允许' if info['permissions']['copy'] else '禁止'}")
            print(f"   - 修改: {'允许' if info['permissions']['modify'] else '禁止'}")
        else:
            print(f"📄 PDF 状态: 未加密")
            
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
