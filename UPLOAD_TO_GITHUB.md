## 上传到 GitHub 的步骤

### 方式一：通过 GitHub 网页上传（最简单）

1. **在 GitHub 创建新仓库**
   - 登录 https://github.com
   - 点击右上角 "+" → "New repository"
   - Repository name: `MyPDF-Manager`
   - Description: `PDF处理工具集 - OpenClaw Skill`
   - 选择 Public（公开）
   - ✅ 勾选 "Add a README file"
   - ✅ 选择 MIT License
   - 点击 "Create repository"

2. **上传文件**
   - 在新仓库页面点击 "uploading an existing file"
   - 将以下文件/文件夹拖拽上传：
     - `SKILL.md`
     - `README.md`
     - `LICENSE`
     - `QUICKSTART.md`
     - `skill.json`
     - `.gitignore`
     - `scripts/` 文件夹
     - `references/` 文件夹
   - 点击 "Commit changes"

---

### 方式二：通过 Git 命令上传

**步骤如下**：

#### 1. 初始化 Git 仓库
```bash
cd ~/.openclaw/workspace/skills/MyPDF-Manager
git init
```

#### 2. 添加文件
```bash
git add SKILL.md README.md LICENSE QUICKSTART.md skill.json .gitignore
git add scripts/ references/
```

#### 3. 创建第一次提交
```bash
git commit -m "Initial commit: MyPDF-Manager v1.0.0

Features:
- PDF 转图片 (pdftoppm)
- PDF 文字提取 (pdftotext)
- PDF 合并 (pdfunite)
- PDF 拆分 (pdfseparate)
- PDF 压缩 (ghostscript)
- OCR 识别 (tesseract)
- 图片转 PDF (imagemagick)

Includes:
- 4 executable scripts
- Installation guide
- MIT License"
```

#### 4. 关联远程仓库
```bash
# 替换 YOUR_USERNAME 为你的 GitHub 用户名
git remote add origin https://github.com/YOUR_USERNAME/MyPDF-Manager.git
git branch -M main
```

#### 5. 推送到 GitHub
```bash
git push -u origin main
```

**如果需要认证**：
```bash
# 方式一：使用 Personal Access Token
git push https://YOUR_TOKEN@github.com/YOUR_USERNAME/MyPDF-Manager.git

# 方式二：配置 Git 凭证
git config --global credential.helper store
git push -u origin main
# 输入用户名和密码（密码使用 Personal Access Token）
```

---

### 方式三：使用 GitHub CLI（推荐）

#### 1. 安装 GitHub CLI
```bash
# Ubuntu/Debian
sudo apt install gh

# macOS
brew install gh
```

#### 2. 登录 GitHub
```bash
gh auth login
```

#### 3. 创建仓库并推送
```bash
cd ~/.openclaw/workspace/skills/MyPDF-Manager

# 创建仓库
gh repo create MyPDF-Manager --public --description "PDF处理工具集 - OpenClaw Skill" --license MIT

# 初始化 Git
git init
git add .
git commit -m "Initial commit: MyPDF-Manager v1.0.0"

# 推送
git push -u origin main
```

---

## 推荐的仓库设置

### 1. 添加 Topics（标签）

在 GitHub 仓库页面添加标签：
- `pdf`
- `pdf-processing`
- `openclaw`
- `openclaw-skill`
- `ocr`
- `tesseract`
- `poppler`
- `ghostscript`

### 2. 创建 Release

```bash
# 创建标签
git tag -a v1.0.0 -m "Release v1.0.0: Initial release"

# 推送标签
git push origin v1.0.0
```

然后在 GitHub 上创建 Release：
- 点击 "Releases" → "Create a new release"
- 选择标签 v1.0.0
- 填写 Release notes

### 3. 添加徽章（可选）

在 README.md 顶部添加：
```markdown
[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/MyPDF-Manager.svg)](https://github.com/YOUR_USERNAME/MyPDF-Manager/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/MyPDF-Manager.svg)](https://github.com/YOUR_USERNAME/MyPDF-Manager/network)
[![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/MyPDF-Manager.svg)](https://github.com/YOUR_USERNAME/MyPDF-Manager/issues)
```

---

## 文件清单

需要上传的文件：
```
MyPDF-Manager/
├── SKILL.md              # 技能主文档（必须）
├── README.md             # 项目说明
├── LICENSE               # MIT 许可证
├── QUICKSTART.md         # 快速开始指南
├── skill.json            # 元数据
├── .gitignore            # Git 忽略文件
├── scripts/              # 脚本文件夹
│   ├── pdf_split.sh
│   ├── pdf_merge.sh
│   ├── pdf_compress.sh
│   └── ocr_recognize.sh
└── references/           # 参考文档
    └── installation-guide.md
```

---

## 需要我帮你执行吗？

选择一个方式：
1. **网页上传** - 你自己操作，我给你步骤
2. **Git 命令** - 我帮你执行 Git 命令（需要你提供 GitHub 用户名）
3. **GitHub CLI** - 我帮你执行 gh 命令（需要你先登录）

**推荐方式一（网页上传），最简单直观。**
