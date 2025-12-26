# 美学工作室 - 部署指南

## ❌ 为什么会出现 "Failed to fetch" 错误？

当你直接双击打开HTML文件时（file:/// 协议），浏览器会阻止API请求，这是安全限制。

## ✅ 解决方案：部署到真实网页

### 方法1：使用 GitHub Pages（推荐，永久免费）

**步骤：**

1. **注册 GitHub 账号**
   - 访问 https://github.com
   - 点击 "Sign up" 注册（如果已有账号，直接登录）

2. **创建新仓库**
   - 点击右上角 "+" → "New repository"
   - Repository name: `aesthetic-studio`
   - 勾选 "Public"
   - 点击 "Create repository"

3. **上传文件**
   - 点击 "uploading an existing file"
   - 拖拽 `aesthetic-studio-pro.html` 到页面
   - **重要：** 上传后，点击文件，点击 "Rename"，改名为 `index.html`
   - 点击 "Commit changes"

4. **启用 GitHub Pages**
   - 点击仓库的 "Settings"
   - 左侧菜单找到 "Pages"
   - Source: 选择 "main" 分支
   - 点击 "Save"

5. **获取链接**
   - 等待1-2分钟
   - 刷新页面，会显示：
   ```
   Your site is live at https://你的用户名.github.io/aesthetic-studio/
   ```
   - 这就是你的永久链接！

**分享给朋友：**
- 复制这个链接发给朋友
- 朋友打开就能直接使用
- 完全免费，永久有效


### 方法2：使用 Vercel（最快，2分钟搞定）

**步骤：**

1. **访问 Vercel**
   - 打开 https://vercel.com
   - 点击 "Sign Up" 注册（用 GitHub 账号登录最方便）

2. **创建项目**
   - 点击 "Add New..." → "Project"
   - 选择 "Import Git Repository"
   - 或者直接拖拽文件夹

3. **部署**
   - 确保文件名是 `index.html`
   - 点击 "Deploy"
   - 等待30秒

4. **获取链接**
   - 部署完成后会显示：
   ```
   https://aesthetic-studio-xxx.vercel.app
   ```
   - 这就是你的网站链接！

**分享给朋友：**
- 复制链接发给朋友
- 自动HTTPS，非常安全
- 全球CDN加速


### 方法3：使用 Netlify（同样简单）

**步骤：**

1. 访问 https://www.netlify.com
2. 注册账号
3. 拖拽整个文件夹到页面
4. 自动部署，获得链接


## 🚀 本地测试方法（开发用）

如果你想在本地测试，需要启动本地服务器：

**方法A：使用 Python（如果已安装）**
```bash
# 在文件所在目录打开终端
python -m http.server 8000

# 然后访问：
http://localhost:8000/aesthetic-studio-pro.html
```

**方法B：使用 VS Code**
1. 安装 "Live Server" 插件
2. 右键HTML文件 → "Open with Live Server"


## 📋 快速对比

| 方法 | 难度 | 时间 | 是否免费 | 永久性 |
|------|------|------|----------|--------|
| GitHub Pages | ⭐⭐ | 5分钟 | ✅ 免费 | ✅ 永久 |
| Vercel | ⭐ | 2分钟 | ✅ 免费 | ✅ 永久 |
| Netlify | ⭐ | 2分钟 | ✅ 免费 | ✅ 永久 |
| 本地服务器 | ⭐⭐⭐ | 1分钟 | ✅ 免费 | ❌ 仅本地 |


## 💡 推荐选择

**如果你：**
- 想要永久链接分享给朋友 → **GitHub Pages**
- 想要最快部署 → **Vercel**
- 只是自己测试 → **本地服务器**


## 🎯 重要提示

1. **文件名必须是 `index.html`**（部署到网站时）
2. **不能直接双击打开HTML文件**（会报错）
3. **必须通过 http:// 或 https:// 访问**（才能调用API）


## ❓ 常见问题

**Q: 为什么本地打开会报错？**
A: 浏览器的CORS安全策略阻止 file:// 协议访问API

**Q: GitHub Pages 多久生效？**
A: 通常1-2分钟，最多5分钟

**Q: 可以用自己的域名吗？**
A: 可以！GitHub Pages 和 Vercel 都支持自定义域名

**Q: 部署后还能修改吗？**
A: 可以！重新上传文件即可，会自动更新
