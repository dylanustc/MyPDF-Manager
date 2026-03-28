# MyPDF-Manager - PDF 智能处理工具集

**OpenClaw Skill for PDF Processing**

---

## 💬 触发词

当用户说以下内容时，触发此技能：

- PDF 处理、PDF 转换、PDF 操作
- PDF 转图片、PDF 提取文字、PDF 合并、PDF 拆分
- PDF 压缩、OCR 识别、扫描 PDF
- 图片转 PDF、批量处理 PDF
- **PDF 转 Word、PDF 转 Excel、Word 转 PDF、Excel 转 PDF**

---

## 🎯 核心功能

### 1. PDF 转图片
**用户说**：
```
帮我把这个 PDF 转成图片
转换 PDF 为 PNG，300 DPI
提取 PDF 每一页为图片
```

**底层命令**：
```bash
pdftoppm -png -r 300 input.pdf output
```

---

### 2. PDF 文字提取
**用户说**：
```
提取这个 PDF 的文字
读取 PDF 内容
把 PDF 转成文本
```

**底层命令**：
```bash
pdftotext input.pdf output.txt
pdftotext -layout input.pdf output.txt  # 保留布局
```

---

### 3. PDF 合并
**用户说**：
```
合并这几个 PDF 文件
把 file1.pdf 和 file2.pdf 合并
合并所有 PDF
```

**底层命令**：
```bash
pdfunite file1.pdf file2.pdf output.pdf
pdfunite *.pdf merged.pdf
```

---

### 4. PDF 拆分
**用户说**：
```
拆分这个 PDF，每页一个文件
提取 PDF 的第 1-5 页
把 PDF 分成多个文件
```

**底层命令**：
```bash
pdfseparate -f 1 -l 5 input.pdf output-%d.pdf
pdfseparate input.pdf page-%d.pdf
```

---

### 5. PDF 压缩
**用户说**：
```
压缩这个 PDF 文件
减小 PDF 体积
优化 PDF 大小
```

**底层命令**：
```bash
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -o output.pdf input.pdf
```

**压缩级别**：
- `/screen` - 72 DPI，最小体积
- `/ebook` - 150 DPI，推荐
- `/printer` - 300 DPI，打印质量
- `/prepress` - 300 DPI，专业印刷

---

### 6. OCR 识别
**用户说**：
```
识别这个扫描 PDF 的文字
OCR 这个图片
把图片 PDF 转成可编辑文字
```

**底层命令**：
```bash
# 识别中文
tesseract input.png output -l chi_sim

# 识别英文
tesseract input.png output -l eng

# 识别中英混合
tesseract input.png output -l chi_sim+eng
```

**处理扫描 PDF 的流程**：
1. PDF 转图片：`pdftoppm -png -r 300 scan.pdf page`
2. OCR 识别：`tesseract page-1.png output -l chi_sim`
3. 合并文本：`cat *.txt > result.txt`

---

### 7. 图片转 PDF
**用户说**：
```
把这些图片转成 PDF
合并图片为一个 PDF
把多张图片合成 PDF
```

**底层命令**：
```bash
convert *.jpg output.pdf
convert image1.png image2.png output.pdf
```

---

### 7. 图片转 PDF
**用户说**：
```
把这些图片转成 PDF
合并图片为一个 PDF
把多张图片合成 PDF
```

**底层命令**：
```bash
convert *.jpg output.pdf
convert image1.png image2.png output.pdf
```

---

### 8. PDF 转 Word ✨ 新功能
**用户说**：
```
把这个 PDF 转成 Word
我需要编辑这个 PDF，转成 docx
PDF 转 Word 文档
```

**底层命令**：
```bash
pdf2docx input.pdf output.docx
```

**效果**：⭐⭐⭐⭐⭐
- ✅ 保留格式、字体、图片、表格
- ✅ 排版几乎无损
- ✅ 支持中文、英文、表格

---

### 9. Word 转 PDF ✨ 新功能
**用户说**：
```
把 Word 转成 PDF
docx 转 PDF
Word 文档转 PDF
```

**底层命令**：
```bash
# 需要 LibreOffice
libreoffice --headless --convert-to pdf input.docx
```

**效果**：⭐⭐⭐⭐⭐ 完美
- ✅ 排版完全保留
- ✅ 字体、图片、表格无损

**注意**：需要安装 LibreOffice
```bash
sudo apt-get install -y libreoffice-writer
```

---

### 10. PDF 转 Excel ✨ 新功能
**用户说**：
```
把这个 PDF 表格转成 Excel
提取 PDF 里的表格数据
PDF 转 xlsx
```

**底层命令**：
```bash
python3 scripts/pdf_to_excel.py input.pdf output.xlsx
```

**效果**：⭐⭐⭐⭐ 好
- ✅ 提取文本和表格
- ✅ 表格识别准确率 80-90%
- ⚠️ 复杂表格可能需要手动调整

---

### 11. Excel 转 PDF ✨ 新功能
**用户说**：
```
把 Excel 转成 PDF
xlsx 转 PDF
Excel 表格转 PDF
```

**底层命令**：
```bash
# 需要 LibreOffice
libreoffice --headless --convert-to pdf input.xlsx
```

**效果**：⭐⭐⭐⭐⭐ 完美
- ✅ 排版完全保留
- ✅ 表格、格式无损

**注意**：需要安装 LibreOffice
```bash
sudo apt-get install -y libreoffice-calc
```

---

### 批量提取文字
**用户说**：
```
批量提取所有 PDF 的文字
处理这个文件夹里的所有 PDF
```

**AI 执行**：
```bash
for pdf in *.pdf; do
  pdftotext "$pdf" "${pdf%.pdf}.txt"
done
```

### 批量压缩
**用户说**：
```
压缩所有 PDF 文件
批量减小 PDF 体积
```

**AI 执行**：
```bash
for pdf in *.pdf; do
  gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -o "compressed_$pdf" "$pdf"
done
```

### 批量转图片
**用户说**：
```
把所有 PDF 都转成图片
批量转换 PDF 为 PNG
```

**AI 执行**：
```bash
for pdf in *.pdf; do
  mkdir -p "${pdf%.pdf}"
  pdftoppm -png -r 150 "$pdf" "${pdf%.pdf}/page"
done
```

---

## 🔧 可执行脚本

### pdf_split.sh
**用法**：
```bash
./scripts/pdf_split.sh input.pdf [起始页] [结束页] [输出前缀]
```

**示例**：
```bash
# 提取第 1-5 页
./scripts/pdf_split.sh document.pdf 1 5 part

# 提取所有页面
./scripts/pdf_split.sh document.pdf
```

---

### pdf_merge.sh
**用法**：
```bash
./scripts/pdf_merge.sh output.pdf input1.pdf input2.pdf ...
```

**示例**：
```bash
./scripts/pdf_merge.sh merged.pdf part1.pdf part2.pdf part3.pdf
```

---

### pdf_compress.sh
**用法**：
```bash
./scripts/pdf_compress.sh input.pdf output.pdf [质量级别]
```

**示例**：
```bash
# 电子书质量（推荐）
./scripts/pdf_compress.sh large.pdf compressed.pdf ebook

# 屏幕质量（最小体积）
./scripts/pdf_compress.sh large.pdf compressed.pdf screen
```

---

### ocr_recognize.sh
**用法**：
```bash
./scripts/ocr_recognize.sh input.pdf output.txt [语言]
```

**示例**：
```bash
# 识别中文
./scripts/ocr_recognize.sh scan.pdf output.txt chi_sim

# 识别中英混合
./scripts/ocr_recognize.sh scan.pdf output.txt chi_sim+eng
```

---

## 💡 使用技巧

### 提示词示例

**场景 1：提取扫描文档**
```
用户：这是一个扫描的合同 PDF，帮我识别文字
AI：
1. 将 PDF 转换为高清图片（300 DPI）
2. 使用 OCR 识别每页文字
3. 合并所有识别结果
4. 返回可编辑文本
```

**场景 2：压缩大型 PDF**
```
用户：这个 PDF 有 50MB，帮我压缩一下
AI：
1. 检查原始大小
2. 使用 ebook 质量压缩
3. 显示压缩率
4. 返回压缩后的文件
```

**场景 3：批量处理**
```
用户：这个文件夹里有 20 个 PDF，全部提取文字
AI：
1. 扫描文件夹，找到所有 PDF
2. 逐个提取文字
3. 保存为对应的文本文件
4. 显示处理进度
```

---

## ⚙️ 依赖工具

| 工具 | 包名 | 功能 | 大小 |
|------|------|------|------|
| pdftoppm | poppler-utils | PDF 转图片 | ~4 MB |
| pdftotext | poppler-utils | 文字提取 | ~4 MB |
| pdfunite | poppler-utils | PDF 合并 | ~4 MB |
| pdfseparate | poppler-utils | PDF 拆分 | ~4 MB |
| tesseract | tesseract-ocr | OCR 识别 | ~1 MB |
| tesseract-ocr-chi-sim | - | 中文语言包 | ~2.5 MB |
| gs | ghostscript | PDF 压缩 | ~24 MB |
| convert | imagemagick | 图片转换 | ~0.5 MB |
| **pdf2docx** | Python 库 | **PDF 转 Word** | ~10 MB |
| **pdfplumber** | Python 库 | **PDF 转 Excel** | ~5 MB |
| **LibreOffice** | libreoffice | **Word/Excel 转 PDF** | ~300 MB |
| **总依赖** | - | - | **~50-70 MB** (不含 LibreOffice) |

---

## 🚀 安装依赖

**Ubuntu/Debian**:
```bash
# 核心工具（必需）
sudo apt-get update
sudo apt-get install -y \
  poppler-utils \
  tesseract-ocr \
  tesseract-ocr-chi-sim \
  ghostscript \
  imagemagick

# PDF ↔ Word/Excel 转换（推荐）
pip3 install pdf2docx pdfplumber --break-system-packages

# Word/Excel → PDF 转换（可选，需要 LibreOffice）
sudo apt-get install -y libreoffice-writer libreoffice-calc
```

**CentOS/RHEL**:
```bash
# 核心工具
sudo yum install -y \
  poppler-utils \
  tesseract \
  ghostscript \
  ImageMagick

# PDF ↔ Word/Excel 转换
pip3 install pdf2docx pdfplumber --break-system-packages

# Word/Excel → PDF 转换（可选）
sudo yum install -y libreoffice-writer libreoffice-calc
```

**macOS**:
```bash
# 核心工具
brew install \
  poppler \
  tesseract \
  ghostscript \
  imagemagick

# PDF ↔ Word/Excel 转换
pip3 install pdf2docx pdfplumber

# Word/Excel → PDF 转换（可选）
brew install --cask libreoffice
```

---

## 📚 参考资料

- [安装指南](references/installation-guide.md) - 详细安装步骤和命令参考
- [快速开始](QUICKSTART.md) - 快速上手指南

---

## 📝 版本历史

**v1.1.0** (2026-03-29)
- ✨ 新增 PDF ↔ Word 双向转换
- ✨ 新增 PDF ↔ Excel 双向转换
- 📝 更新文档，添加格式转换说明
- 🔧 新增 4 个转换脚本

**v1.0.0** (2026-03-29)
- 初始版本
- 支持 PDF 转图片、文字提取、合并、拆分、压缩、OCR、图片转 PDF
- 包含 4 个可执行脚本
- 完整的安装指南和文档

---

**License**: MIT
**Author**: dylanustc
**GitHub**: https://github.com/dylanustc/MyPDF-Manager
