---
name: MyPDF-Manager
description: PDF处理工具集，支持PDF转换、合并、拆分、压缩、文字提取、OCR识别、图片转换。触发词：PDF处理、PDF转换、PDF合并、PDF拆分、PDF压缩、提取文字、OCR识别、图片转PDF、PDF转图片。使用场景：(1) PDF文件处理和转换 (2) 文档数字化和OCR (3) PDF合并拆分 (4) PDF压缩优化。
---

# MyPDF-Manager - PDF 处理工具集

PDF智能处理工具，基于系统级命令行工具（poppler-utils, tesseract-ocr, ghostscript, imagemagick）提供完整的 PDF 处理能力。

## 核心功能

### 1. PDF 转图片
**工具**: `pdftoppm`
**用法**: 将 PDF 每一页渲染为高质量图片

```bash
# 转换所有页面为 PNG（300 DPI 高清）
pdftoppm -png -r 300 input.pdf output

# 只转换第 1-5 页
pdftoppm -png -f 1 -l 5 input.pdf output

# 转换为 JPEG 格式
pdftoppm -jpeg -r 150 input.pdf output
```

**输出**: `output-1.png`, `output-2.png`, ...

### 2. PDF 文字提取
**工具**: `pdftotext`
**用法**: 提取 PDF 中的文本内容

```bash
# 基本提取
pdftotext input.pdf output.txt

# 保留原始布局
pdftotext -layout input.pdf output.txt

# 指定编码
pdftotext -enc UTF-8 input.pdf output.txt

# 只提取第 3-8 页
pdftotext -f 3 -l 8 input.pdf output.txt
```

**注意**: 
- 扫描 PDF 需要先用 OCR 识别
- 多栏布局可能导致文字乱序
- 嵌入字体可能影响识别

### 3. PDF 合并
**工具**: `pdfunite`
**用法**: 将多个 PDF 合并成一个

```bash
# 合并多个文件
pdfunite file1.pdf file2.pdf file3.pdf output.pdf

# 合并当前目录所有 PDF
pdfunite *.pdf merged.pdf
```

**特点**: 不重新编码，保留原始质量，速度快

### 4. PDF 拆分
**工具**: `pdfseparate`
**用法**: 提取 PDF 的指定页面

```bash
# 提取第 1-5 页，每页一个文件
pdfseparate -f 1 -l 5 input.pdf output-%d.pdf

# 提取所有页面
pdfseparate input.pdf page-%d.pdf

# 提取单页（第 3 页）
pdfseparate -f 3 -l 3 input.pdf page3.pdf
```

**输出**: `output-1.pdf`, `output-2.pdf`, ...

### 5. PDF 压缩
**工具**: `ghostscript` (gs)
**用法**: 压缩 PDF 文件体积

```bash
# 屏幕质量（72 DPI，最小体积）
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/screen -o output.pdf input.pdf

# 电子书质量（150 DPI，推荐）
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -o output.pdf input.pdf

# 打印质量（300 DPI）
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/printer -o output.pdf input.pdf

# 预印质量（300 DPI，最高质量）
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -o output.pdf input.pdf
```

**压缩级别说明**:
- `/screen` - 最小体积，适合屏幕阅读
- `/ebook` - 平衡质量和体积，推荐
- `/printer` - 打印质量
- `/prepress` - 专业印刷质量

### 6. OCR 识别
**工具**: `tesseract`
**用法**: 识别图片或扫描 PDF 中的文字

```bash
# 识别中文
tesseract input.png output -l chi_sim

# 识别英文
tesseract input.png output -l eng

# 识别中英文混合
tesseract input.png output -l chi_sim+eng

# 输出 PDF（带文字层）
tesseract input.png output -l chi_sim pdf

# 输出带位置信息的 HTML
tesseract input.png output -l chi_sim hocr
```

**支持语言**: 
- `chi_sim` - 中文简体
- `chi_tra` - 中文繁体
- `eng` - 英文
- `jpn` - 日文
- 等 100+ 种语言

**扫描 PDF 处理流程**:
```bash
# 1. PDF 转图片
pdftoppm -png input.pdf page

# 2. OCR 识别每页
for f in page-*.png; do
  tesseract "$f" "${f%.png}" -l chi_sim
done

# 3. 合并文本
cat page-*.txt > output.txt
```

### 7. 图片转 PDF
**工具**: `imagemagick` (convert)
**用法**: 将图片转换为 PDF

```bash
# 单张图片转 PDF
convert input.jpg output.pdf

# 多张图片合并为一个 PDF
convert image1.jpg image2.jpg image3.jpg output.pdf

# 所有图片转 PDF
convert *.jpg output.pdf

# 调整图片大小后转换
convert input.jpg -resize 800x600 output.pdf
```

### 8. PDF 信息查看
**工具**: `pdfinfo`
**用法**: 查看 PDF 元数据

```bash
# 查看基本信息
pdfinfo input.pdf

# 输出示例：
# Title:          文档标题
# Author:         作者
# Creator:        创建工具
# Producer:       生成工具
# CreationDate:   创建时间
# ModDate:        修改时间
# Pages:          页数
# Page size:      页面大小
# File size:      文件大小
```

## 使用场景

### 场景 1: 扫描文档数字化
```bash
# 步骤 1: PDF 转图片
pdftoppm -png -r 300 scan.pdf page

# 步骤 2: OCR 识别
for f in page-*.png; do
  tesseract "$f" "${f%.png}" -l chi_sim
done

# 步骤 3: 合并文本
cat page-*.txt > digitized.txt
```

### 场景 2: 批量处理 PDF
```bash
# 批量提取文字
for pdf in *.pdf; do
  pdftotext "$pdf" "${pdf%.pdf}.txt"
done

# 批量压缩
for pdf in *.pdf; do
  gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -o "compressed_$pdf" "$pdf"
done
```

### 场景 3: PDF 处理工作流
```bash
# 1. 拆分 PDF
pdfseparate -f 1 -l 10 large.pdf part-%d.pdf

# 2. 提取文字
for f in part-*.pdf; do
  pdftotext "$f" "${f%.pdf}.txt"
done

# 3. 合并需要的部分
pdfunite part-1.pdf part-3.pdf part-5.pdf selected.pdf

# 4. 压缩输出
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -o final.pdf selected.pdf
```

## 依赖工具

| 工具 | 包名 | 功能 |
|------|------|------|
| pdftoppm | poppler-utils | PDF 转图片 |
| pdftotext | poppler-utils | PDF 文字提取 |
| pdfunite | poppler-utils | PDF 合并 |
| pdfseparate | poppler-utils | PDF 拆分 |
| pdfinfo | poppler-utils | PDF 信息查看 |
| tesseract | tesseract-ocr | OCR 识别 |
| tesseract-ocr-chi-sim | tesseract-ocr-chi-sim | 中文语言包 |
| gs | ghostscript | PDF 压缩 |
| convert | imagemagick | 图片转换 |

## 安装方法

**Ubuntu/Debian**:
```bash
sudo apt-get update
sudo apt-get install -y poppler-utils tesseract-ocr tesseract-ocr-chi-sim ghostscript imagemagick
```

**CentOS/RHEL**:
```bash
sudo yum install -y poppler-utils tesseract ghostscript ImageMagick
```

**macOS**:
```bash
brew install poppler tesseract ghostscript imagemagick
```

## 注意事项

1. **扫描 PDF**: 没有文字层，需要先用 OCR 识别
2. **多栏布局**: pdftotext 可能导致文字乱序
3. **嵌入字体**: 特殊字体可能影响文字提取
4. **图片质量**: OCR 识别效果取决于图片清晰度
5. **文件大小**: 高 DPI 转换会生成大文件
6. **权限问题**: ImageMagick 可能需要配置权限策略

## 常见问题

### Q: OCR 识别效果不好？
A: 尝试提高图片分辨率（-r 300），或预处理图片（灰度化、二值化）

### Q: 文字提取乱序？
A: 使用 `-layout` 参数保留原始布局

### Q: 压缩后质量下降？
A: 使用更高的压缩级别（/printer 或 /prepress）

### Q: ImageMagick 报错？
A: 检查权限策略文件 `/etc/ImageMagick-6/policy.xml`

### Q: Tesseract 不支持某语言？
A: 安装对应语言包：`sudo apt-get install tesseract-ocr-<lang>`
