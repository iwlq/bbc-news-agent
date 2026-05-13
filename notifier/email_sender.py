# notifier/email_sender.py
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

def send_email(report_content):
    """
    接收最终的分析报告文本，并发送到指定邮箱
    """
    print("正在准备发送邮件...")

    # 1. 基础配置（以 QQ 邮箱为例，如果是 163 请换成 smtp.163.com）
    smtp_server = "smtp.qq.com"
    smtp_port = 465  # SSL 安全加密端口

    # 你的发件人账号和刚刚获取的【授权码】（千万不是登录密码！）
    sender_email = "******@qq.com"
    auth_code = "授权码"

    # 收件人（如果是发给自己，可以和发件人一样）
    receiver_email = ["收件人邮箱"]

    # 2. 构建邮件内容
    # MIMEText(邮件正文, 文本格式, 编码)
    message = MIMEText(report_content, 'plain', 'utf-8')
    message['From'] = formataddr(["🤖 你的AI新闻助理", sender_email])
    message['To'] = Header("Boss", 'utf-8')
    message['Subject'] = Header("🌍 今日BBC全球重点新闻与深度解读", 'utf-8')  # 邮件标题

    # 3. 连接服务器并发送
    try:
        # 使用 SSL 加密连接
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, auth_code)
        server.sendmail(sender_email, [receiver_email], message.as_string())
        server.quit()
        print("✅ 邮件发送成功！请查收。")
    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")