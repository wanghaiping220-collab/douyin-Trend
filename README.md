# 抖音热榜定时推送到飞书

这个项目可以定时抓取抖音热榜数据，并通过 Webhook 推送到飞书群聊。

## 功能特性

- ⏰ 定时抓取抖音热榜（默认每小时一次）
- 📊 获取最新的热门话题和热度值
- 🤖 自动推送到飞书群聊
- 💬 支持多种消息格式（文本、富文本、交互式卡片）
- 📝 完整的日志记录
- 🐳 支持 Docker 部署

## 项目结构

```
.
├── main.py                 # 主程序入口
├── douyin_scraper.py       # 抖音热榜抓取模块
├── feishu_notifier.py      # 飞书通知模块
├── requirements.txt        # Python 依赖
├── .env.example           # 环境变量示例
├── .gitignore             # Git 忽略文件
├── Dockerfile             # Docker 镜像配置
├── docker-compose.yml     # Docker Compose 配置
└── README.md              # 项目说明
```

## 快速开始

### 前置要求

- Python 3.8+
- 飞书机器人 Webhook URL

### 获取飞书 Webhook URL

1. 在飞书群聊中，点击右上角设置按钮
2. 选择「群机器人」->「添加机器人」
3. 选择「自定义机器人」
4. 设置机器人名称和描述
5. 复制生成的 Webhook URL

### 安装和配置

#### 方法一：本地运行

1. **克隆项目**

```bash
git clone <your-repo-url>
cd New-repository
```

2. **安装依赖**

```bash
pip install -r requirements.txt
```

3. **配置环境变量**

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，填入你的飞书 Webhook URL
# FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/your-webhook-url
```

4. **运行程序**

```bash
python main.py
```

#### 方法二：Docker 部署

1. **配置环境变量**

```bash
cp .env.example .env
# 编辑 .env 文件，填入配置
```

2. **使用 Docker Compose 启动**

```bash
docker-compose up -d
```

3. **查看日志**

```bash
docker-compose logs -f
```

4. **停止服务**

```bash
docker-compose down
```

## 配置说明

在 `.env` 文件中可以配置以下参数：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `FEISHU_WEBHOOK_URL` | 飞书机器人 Webhook URL | 必填 |
| `SCRAPE_INTERVAL_HOURS` | 抓取间隔（小时） | 1 |
| `LOG_LEVEL` | 日志级别（DEBUG/INFO/WARNING/ERROR） | INFO |

## 测试模块

### 测试抖音热榜抓取

```bash
python douyin_scraper.py
```

### 测试飞书消息发送

```bash
# 需要先配置 .env 文件
python feishu_notifier.py
```

## 消息格式示例

程序会发送类似以下格式的消息到飞书群：

```
📊 抖音热榜 Top10 (2024-01-22 10:00:00)

🥇 热门话题1 [热] 🔥1.2亿
🥈 热门话题2 🔥8500万
🥉 热门话题3 [新] 🔥6200万
4. 热门话题4 🔥4800万
...
```

## 常见问题

### 1. 如何修改抓取间隔？

编辑 `.env` 文件中的 `SCRAPE_INTERVAL_HOURS` 参数。

### 2. 为什么收不到消息？

- 检查 Webhook URL 是否正确
- 检查网络连接是否正常
- 查看日志文件 `douyin_hot_scraper.log` 获取详细错误信息

### 3. 如何在后台运行？

**使用 screen 或 tmux：**

```bash
screen -S douyin-scraper
python main.py
# 按 Ctrl+A 然后按 D 离开 screen
```

**使用 systemd（Linux）：**

创建服务文件 `/etc/systemd/system/douyin-scraper.service`：

```ini
[Unit]
Description=Douyin Hot List Scraper
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/New-repository
ExecStart=/usr/bin/python3 /path/to/New-repository/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

启动服务：

```bash
sudo systemctl enable douyin-scraper
sudo systemctl start douyin-scraper
```

## 开发说明

### 项目依赖

- `requests`: HTTP 请求库
- `schedule`: 任务调度库
- `python-dotenv`: 环境变量管理
- `pyyaml`: YAML 配置文件支持

### 添加新功能

1. 修改 `douyin_scraper.py` 添加新的抓取功能
2. 修改 `feishu_notifier.py` 添加新的消息格式
3. 在 `main.py` 中集成新功能

## 注意事项

- 请遵守抖音的使用条款和 robots.txt
- 不要过于频繁地请求，建议间隔至少 1 小时
- 抖音 API 可能会变化，如遇问题请及时更新
- 确保服务器网络稳定，能够访问抖音和飞书 API

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 更新日志

### v1.0.0 (2024-01-22)

- 初始版本发布
- 支持定时抓取抖音热榜
- 支持推送到飞书群
- 支持 Docker 部署
