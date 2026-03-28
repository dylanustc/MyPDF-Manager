# MyPDF-Manager

<div align="center">

**PDF 智能处理工具集**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue.svg)](https://openclaw.ai)

</div>

---

## 📖 简介

MyPDF-Manager 是一个功能强大的 PDF 处理工具集，基于系统级命令行工具提供完整的 PDF 处理能力。

**核心功能**：
- 🔄 **PDF 转图片** - 高质量渲染，支持多种格式
- 📝 **文字提取** - 从 PDF 提取纯文本
- 📑 **PDF 合并** - 多文件合并为一个
- ✂️ **PDF 拆分** - 提取指定页面
- 🗜️ **PDF 压缩** - 减小文件体积
- 🔍 **OCR 识别** - 识别扫描文档中的文字
- 🖼️ **图片转 PDF** - 多图合并为 PDF

## ✨ 特性

- ✅ **完全免费** - 基于开源工具，无需付费
- ✅ **离线使用** - 无需网络，本地处理
- ✅ **批量处理** - 支持批量操作
- ✅ **多平台支持** - Ubuntu/Debian、CentOS/RHEL、macOS
- ✅ **高质量输出** - 支持 300+ DPI
- ✅ **多语言 OCR** - 支持中文、英文、日文等 100+ 种语言

## 🚀 快速开始

### 安装依赖

**Ubuntu/Debian**:
```bash
sudo apt-get update
sudo apt-get install -y \
  poppler-utils \
  tesseract-ocr \
  tesseract-ocr-chi-sim \
  ghostscript \
  imagemagick
```

**CentOS/RHEL**:
```bash
sudo yum install -y \
  poppler-utils \
  tesseract \
  ghostscript \
  ImageMagick
```

**macOS**:
```bash
brew install \
  poppler \
  tesseract \
  ghostscript \
  imagemagick
```

### 使用方法

#### 1. PDF 转图片
```bash
pdftoppm -png -r 300 input.pdf output
```

#### 2. PDF 文字提取
```bash
pdftotext input.pdf output.txt
```

#### 3. PDF 合并
```bash
pdfunite file1.pdf file2.pdf output.pdf
```

#### 4. PDF 拆分
```bash
pdfseparate -f 1 -l 5 input.pdf output-%d.pdf
```

#### 5. PDF 压缩
```bash
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -o output.pdf input.pdf
```

#### 6. OCR 识别
```bash
tesseract input.png output -l chi_sim
```

#### 7. 图片转 PDF
```bash
convert *.jpg output.pdf
```

## 📁 文件结构

```
MyPDF-Manager/
├── SKILL.md                      # 主文档
├── README.md                     # 本文件
├── LICENSE                       # MIT 许可证
├── skill.json                    # 元数据
├── scripts/                      # 可执行脚本
│   ├── pdf_split.sh             # PDF 拆分脚本
│   ├── pdf_merge.sh             # PDF 合并脚本
│   ├── pdf_compress.sh          # PDF 压缩脚本
│   └── ocr_recognize.sh         # OCR 识别脚本
└── references/                   # 参考文档
    └── installation-guide.md    # 安装指南
```

## 🛠️ 脚本使用

### PDF 拆分
```bash
./scripts/pdf_split.sh input.pdf [起始页] [结束页] [输出前缀]

# 示例
./scripts/pdf_split.sh document.pdf 1 5 part
```

### PDF 合并
```bash
./scripts/pdf_merge.sh output.pdf input1.pdf input2.pdf ...

# 示例
./scripts/pdf_merge.sh merged.pdf part1.pdf part2.pdf part3.pdf
```

### PDF 压缩
```bash
./scripts/pdf_compress.sh input.pdf output.pdf [质量级别]

# 示例
./scripts/pdf_compress.sh large.pdf compressed.pdf ebook
```

### OCR 识别
```bash
./scripts/ocr_recognize.sh input.pdf output.txt [语言]

# 示例
./scripts/ocr_recognize.sh scan.pdf output.txt chi_sim
```

## 📋 批量处理

### 批量提取文字
```bash
for pdf in *.pdf; do
  pdftotext "$pdf" "${pdf%.pdf}.txt"
done
```

### 批量压缩
```bash
for pdf in *.pdf; do
  gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -o "compressed_$pdf" "$pdf"
done
```

### 批量转图片
```bash
for pdf in *.pdf; do
  mkdir -p "${pdf%.pdf}"
  pdftoppm -png -r 150 "$pdf" "${pdf%.pdf}/page"
done
```

## 🔧 依赖工具

| 工具 | 包名 | 功能 |
|------|------|------|
| pdftoppm | poppler-utils | PDF 转图片 |
| pdftotext | poppler-utils | PDF 文字提取 |
| pdfunite | poppler-utils | PDF 合并 |
| pdfseparate | poppler-utils | PDF 拆分 |
| tesseract | tesseract-ocr | OCR 识别 |
| gs | ghostscript | PDF 压缩 |
| convert | imagemagick | 图片转换 |

## ⚙️ 配置

### OCR 语言包

**安装其他语言**:
```bash
# 日文
sudo apt-get install tesseract-ocr-jpn

# 韩文
sudo apt-get install tesseract-ocr-kor

# 法文
sudo apt-get install tesseract-ocr-fra

# 查看所有语言
apt-cache search tesseract-ocr
```

### ImageMagick 权限

如果遇到权限问题，编辑 `/etc/ImageMagick-6/policy.xml`:
```xml
<!-- 注释掉或修改 -->
<policy domain="coder" rights="read|write" pattern="PDF" />
```

## 📊 性能

| 操作 | 速度 | 质量 |
|------|------|------|
| PDF 转图片 (300 DPI) | ~1s/页 | 高 |
| 文字提取 | ~0.1s/页 | 依赖字体 |
| PDF 合并 | ~0.5s/文件 | 无损 |
| PDF 压缩 | ~2s/页 | 可调节 |
| OCR 识别 (300 DPI) | ~5s/页 | 98%+ |

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📝 许可证

本项目采用 [MIT 许可证](LICENSE)。

## 🙏 致谢

- [Poppler](https://poppler.freedesktop.org/) - PDF 渲染库
- [Tesseract](https://github.com/tesseract-ocr/tesseract) - OCR 引擎
- [Ghostscript](https://www.ghostscript.com/) - PDF 处理
- [ImageMagick](https://imagemagick.org/) - 图片处理

---

**Made with ❤️ for OpenClaw**
