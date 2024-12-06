import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 邮件设置
sender_email = "chesih24@aiglon.ch"
receiver_email = "zhaban24@aiglon.ch"
password = "CHESIH24"

# 创建邮件对象
message = MIMEMultipart()
message["From"] = chesih24@aiglon.ch
message["To"] = zhaban24@aiglon.ch
message["Subject"] = "问候"

# 邮件内容
body = "你好这是一份测试邮件"
message.attach(MIMEText(body, "plain"))

# 发送邮件
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)  # 你可以替换为你使用的邮件服务提供商的SMTP服务器地址
    server.starttls(TLS)  # 启动TLS加密
    server.login(chesih24@aiglon.ch, CHESIH24)  # 登录到邮件服务器
    server.sendmail(sender_email, receiver_email, message.as_string())  # 发送邮件
    print("邮件发送成功")
except Exception as e:
    print(f"邮件发送失败: {e}")
finally:
    server.quit()  # 退出SMTP服务器
