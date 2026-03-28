# PDF 处理命令快速参考

## 安装命令

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install -y poppler-utils tesseract-ocr tesseract-ocr-chi-sim ghostscript imagemagick
```

### CentOS/RHEL
```bash
sudo yum install -y poppler-utils tesseract ghostscript ImageMagick
```

### macOS
```bash
brew install poppler tesseract ghostscript imagemagick
```

### 验证安装
```bash
# 检查所有工具是否安装成功
which pdftoppm pdftotext pdfunite pdfseparate tesseract gs convert

# 查看版本
pdftotext -v
tesseract --version
gs --version
convert --version
```

## 常用命令速查表

### PDF 转图片
```bash
pdftoppm -png -r 300 input.pdf output        # 高清 PNG (300 DPI)
pdftoppm -jpeg -r 150 input.pdf output       # JPEG (150 DPI)
pdftoppm -png -f 1 -l 5 input.pdf output     # 只转第 1-5 页
```

### PDF 文字提取
```bash
pdftotext input.pdf output.txt               # 基本提取
pdftotext -layout input.pdf output.txt       # 保留布局
pdftotext -f 3 -l 8 input.pdf output.txt     # 只提取第 3-8 页
```

### PDF 合并
```bash
pdfunite file1.pdf file2.pdf output.pdf      # 合并两个文件
pdfunite *.pdf merged.pdf                    # 合并所有 PDF
```

### PDF 拆分
```bash
pdfseparate -f 1 -l 5 input.pdf output-%d.pdf   # 提取第 1-5 页
pdfseparate input.pdf page-%d.pdf               # 提取所有页面
```

### PDF 压缩
```bash
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/screen -o output.pdf input.pdf    # 最小体积
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -o output.pdf input.pdf     # 推荐
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/printer -o output.pdf input.pdf   # 打印质量
```

### OCR 识别
```bash
tesseract input.png output -l chi_sim        # 中文
tesseract input.png output -l eng            # 英文
tesseract input.png output -l chi_sim+eng    # 中英混合
```

### 图片转 PDF
```bash
convert input.jpg output.pdf                 # 单张图片
convert *.jpg output.pdf                     # 所有图片
convert image1.jpg image2.jpg output.pdf     # 指定图片
```

### PDF 信息
```bash
pdfinfo input.pdf                            # 查看信息
```

## 批量处理脚本

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

## 磁盘空间需求

- **poppler-utils**: ~4 MB
- **tesseract-ocr**: ~1 MB
- **tesseract-ocr-chi-sim**: ~2.5 MB
- **ghostscript**: ~24 MB
- **imagemagick**: ~0.5 MB
- **总依赖**: ~50-70 MB

## 常见问题

### Q: 如何查看已安装的语言包？
```bash
tesseract --list-langs
```

### Q: 如何安装其他语言包？
```bash
# Ubuntu/Debian
sudo apt-get install tesseract-ocr-jpn    # 日文
sudo apt-get install tesseract-ocr-kor    # 韩文
sudo apt-get install tesseract-ocr-fra    # 法文

# 查看所有可用语言包
apt-cache search tesseract-ocr
```

### Q: ImageMagick 报错怎么办？
```bash
# 编辑权限策略文件
sudo nano /etc/ImageMagick-6/policy.xml

# 注释掉或修改以下行
<!-- <policy domain="coder" rights="none" pattern="PDF" /> -->
```

### Q: 如何提高 OCR 准确率？
```bash
# 1. 提高分辨率
pdftoppm -png -r 600 input.pdf output  # 600 DPI

# 2. 预处理图片（灰度化、二值化）
convert input.png -colorspace Gray -threshold 50% output.png

# 3. 使用更好的模型
tesseract output.png result -l chi_sim --psm 6
```
