# MyPDF-Manager

<div align="center">

**PDF 智能处理工具 - OpenClaw Skill**

</div>

---

## 📖 简介

MyPDF-Manager 是一个为 OpenClaw 设计的 PDF 处理技能，让你可以通过自然语言对话轻松处理 PDF 文件。

**核心功能**：
- 🔄 **PDF 转图片** - 高质量渲染，支持多种格式
- 📝 **文字提取** - 从 PDF 提取纯文本
- 📑 **PDF 合并** - 多文件合并为一个
- ✂️ **PDF 拆分** - 提取指定页面
- 🗜️ **PDF 压缩** - 减小文件体积
- 🔍 **OCR 识别** - 识别扫描文档中的文字
- 🖼️ **图片转 PDF** - 多图合并为 PDF

## ✨ 特性

- ✅ **对话式交互**   - 用自然语言描述需求，无需命令行
- ✅ **完全免费**    - 基于开源工具，无需付费
- ✅ **离线使用**    - 无需网络，本地处理
- ✅ **批量处理**    - 支持批量操作
- ✅ **多平台支持**  - Ubuntu/Debian、CentOS/RHEL、macOS
- ✅ **高质量输出**  - 支持 300+ DPI
- ✅ **多语言 OCR** - 支持中文、英文、日文等 100+ 种语言

## 💬 在飞书对话中使用

### 方式一：直接对话（推荐）

在飞书、Telegram、Discord 等平台与 OpenClaw 对话时，直接描述你的需求：

**PDF 转图片**：
```
帮我把这个 PDF 转成图片
把 PDF 每一页转成 PNG
转换这个 PDF，分辨率 300 DPI
```

**PDF 文字提取**：
```
提取这个 PDF 里的文字
帮我读取 PDF 的内容
把 PDF 转成文本文件
```

**PDF 合并**：
```
帮我合并这几个 PDF 文件
把 file1.pdf 和 file2.pdf 合并成一个
合并所有 PDF 文件
```

**PDF 拆分**：
```
拆分这个 PDF，每页一个文件
提取 PDF 的第 1-5 页
把这个 PDF 拆开
```

**PDF 压缩**：
```
压缩这个 PDF 文件
减小 PDF 的体积
优化 PDF 大小
```

**OCR 识别**：
```
识别这个扫描 PDF 的文字
OCR 这个 PDF
把图片 PDF 转成可编辑文字
```

**图片转 PDF**：
```
把这些图片转成 PDF
合并图片为 PDF
把多张图片合成一个 PDF
```

**批量处理**：
```
批量提取所有 PDF 的文字
压缩这个文件夹里的所有 PDF
把所有图片都转成 PDF
```

### 方式二：发送文件后描述

1. 在对话中发送 PDF 文件
2. 描述你的需求：
   ```
   帮我提取这个 PDF 的文字
   压缩这个 PDF
   把这个 PDF 转成图片
   ```

### 方式三：询问功能

```
你能处理 PDF 吗？
MyPDF-Manager 有什么功能？
怎么提取 PDF 文字？
```

## 🚀 安装

```bash
git clone https://github.com/dylanustc/MyPDF-Manager.git
```

1. 下载 [MyPDF-Manager.tar.gz]
2. 解压到 `~/.openclaw/workspace/skills/MyPDF-Manager/`
3. 安装依赖工具：

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

## 📁 文件结构

```
MyPDF-Manager/
├── SKILL.md                      # 技能主文档（OpenClaw 读取）
├── README.md                     # 本文件
├── LICENSE                       # MIT 许可证
├── QUICKSTART.md                 # 快速开始指南
├── skill.json                    # 元数据
├── scripts/                      # 可执行脚本
│   ├── pdf_split.sh             # PDF 拆分脚本
│   ├── pdf_merge.sh             # PDF 合并脚本
│   ├── pdf_compress.sh          # PDF 压缩脚本
│   └── ocr_recognize.sh         # OCR 识别脚本
└── references/                   # 参考文档
    └── installation-guide.md    # 详细安装指南
```

## 🎯 使用场景

### 场景 1：扫描文档数字化

**User**：
```
这是一个扫描的 PDF，帮我识别文字
```

**Openclaw**：
1. PDF 转图片
2. OCR 识别每页
3. 合并文字结果
4. 返回可编辑文本

### 场景 2：批量处理

**User**：
```
这个文件夹有 10 个 PDF，帮我全部提取文字
```

**Openclaw**：
1. 遍历所有 PDF
2. 批量提取文字
3. 保存为文本文件

### 场景 3：PDF 压缩

**User**：
```
这个 PDF 太大了，帮我压缩一下
```

**Openclaw**：
1. 检查文件大小
2. 使用 ebook 质量压缩
3. 返回压缩后的文件

### 场景 4：PDF 拆分与合并

**User**：
```
这个 PDF 太长，我只想要第 5-10 页
```

**Openclaw**：
1. 提取第 5-10 页
2. 生成新的 PDF
3. 返回给你

## 🔧 底层工具（高级用户）

MyPDF-Manager 基于以下开源工具：

| 工具 | 功能 |
|------|------|
| **pdftoppm** | PDF 转图片 |
| **pdftotext** | PDF 文字提取 |
| **pdfunite** | PDF 合并 |
| **pdfseparate** | PDF 拆分 |
| **ghostscript** | PDF 压缩 |
| **tesseract** | OCR 识别 |
| **imagemagick** | 图片转换 |

### 命令行使用

如果你想直接使用命令行，可以调用脚本：

```bash
# PDF 拆分
./scripts/pdf_split.sh input.pdf 1 5 part

# PDF 合并
./scripts/pdf_merge.sh output.pdf file1.pdf file2.pdf

# PDF 压缩
./scripts/pdf_compress.sh input.pdf output.pdf ebook

# OCR 识别
./scripts/ocr_recognize.sh input.pdf output.txt chi_sim
```
## 📋 依赖安装验证

```bash
# 检查核心工具
which pdftoppm pdftotext pdfunite pdfseparate tesseract gs convert

# 查看版本
pdftotext -v
tesseract --version
gs --version
convert --version

# 检查语言包
tesseract --list-langs
```

### 安装其他语言包

```bash
# Ubuntu/Debian
sudo apt-get install tesseract-ocr-jpn    # 日文
sudo apt-get install tesseract-ocr-kor    # 韩文
sudo apt-get install tesseract-ocr-fra    # 法文

# 查看所有可用语言
apt-cache search tesseract-ocr
```

## 📊 性能参考

| 操作 | 速度 | 质量 |
|------|------|------|
| PDF 转图片 (300 DPI) | ~1s/页 | 高 |
| 文字提取 | ~0.1s/页 | 依赖字体 |
| PDF 合并 | ~0.5s/文件 | 无损 |
| PDF 压缩 | ~2s/页 | 可调节 |
| OCR 识别 (300 DPI) | ~5s/页 | 98%+ |

## ❓ 常见问题

### Q: OCR 识别效果不好？
A: 尝试提高图片分辨率（-r 300 或更高），或预处理图片（灰度化、二值化）

### Q: 文字提取乱序？
A: 使用 `-layout` 参数保留原始布局

### Q: 压缩后质量下降？
A: 使用更高的压缩级别（/printer 或 /prepress）

### Q: ImageMagick 报错？
A: 编辑 `/etc/ImageMagick-6/policy.xml`，修改 PDF 权限

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📝 许可证

本项目采用 [MIT 许可证](LICENSE)。

## 🙏 致谢

- [Poppler](https://poppler.freedesktop.org/) - PDF 渲染库
- [Tesseract](https://github.com/tesseract-ocr/tesseract) - OCR 引擎
- [Ghostscript](https://www.ghostscript.com/) - PDF 处理
- [ImageMagick](https://imagemagick.org/) - 图片处理
- [OpenClaw](https://openclaw.ai) - AI Agent 平台
