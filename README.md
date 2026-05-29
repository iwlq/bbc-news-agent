# BBC News Agent (AI-Powered) 🌍🤖

![Python >=3.10](https://img.shields.io/badge/Python->=3.10-blue.svg)
![DrissionPage](https://img.shields.io/badge/Powered%20by-DrissionPage-orange.svg)
![ZhipuAI](https://img.shields.io/badge/AI-Zhipu%20GLM--4-red.svg)

`bbc-news-agent` 是一个全自动化的新闻获取与智能分析工具。它能够自动抓取 BBC News 的最新热门资讯，利用大语言模型（GLM-4）进行深度解读，并将精炼后的双语报告通过邮件直接发送到您的收件箱。

## ✨ 核心特性

- **🕷️ 智能爬虫**: 基于 `DrissionPage` 实现的高效浏览器自动化抓取，精准提取 BBC "Most Read" 板块的标题、正文及原文链接。
- **🧠 AI 深度分析**: 集成智谱 AI (ZhipuAI GLM-4) 模型：
  - **新闻速览**: 每条新闻极简一句话概括。
  - **专业翻译**: 高质量的标题与正文中英互译。
  - **首席分析师洞察**: 跨新闻的宏观趋势提炼与地缘政治/经济维度的深度解读。
- **📧 自动邮件递送**: 自动构建精美的文本报告，并通过 SMTP（如 QQ/163 邮箱）安全发送。
- **🧩 模块化设计**: 爬虫、AI 分析、通知推送各司其职，易于维护与扩展。

## 📁 目录结构

```text
bbc-news-agent/
├── main.py                # 项目入口，统筹调度各模块
├── crawler/               # 爬虫模块
│   └── bbc_crawler.py     # 负责抓取 BBC 网页数据
├── ai_analysis/           # AI 处理模块
│   └── zhipu_ai_analysis.py # 负责调用 GLM-4 进行翻译与分析
└── notifier/              # 通知模块
    └── email_sender.py    # 负责 SMTP 邮件发送
```

## 🚀 快速开始

### 前置要求

1. **Python 3.10+**
2. **浏览器环境**: 需安装 Chrome 或 Edge 浏览器（DrissionPage 驱动所需）。
3. **API Key**: 需申请 [智谱 AI](https://open.bigmodel.cn/) 的 API Key。
4. **邮箱授权码**: 开启发件邮箱的 SMTP 服务并获取授权码。

### 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/iwlq/bbc-news-agent.git
   cd bbc-news-agent
   ```

2. **安装依赖**
   ```bash
   pip install DrissionPage zhipuai
   ```

3. **配置参数**
   - 在 `ai_analysis/zhipu_ai_analysis.py` 中填入你的 `api_key`。
   - 在 `notifier/email_sender.py` 中配置发件人邮箱、授权码及收件人。

### 运行

```bash
python main.py
```

## 🛠️ 技术栈

- **自动化框架**: [DrissionPage](https://drissionpage.cn/) (结合了 Selenium 与 requests 的优点)
- **大模型 API**: [ZhipuAI (GLM-4)](https://open.bigmodel.cn/)
- **邮件服务**: `smtplib` + `email` (标准库)

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE) 授权。
