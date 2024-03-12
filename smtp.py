from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from aiosmtplib import SMTP


EMAIL = 'your-email'
PWD = 'your-passw'

async def send_mail(subject, to, msg):
    message = MIMEMultipart()
    message["From"] = EMAIL
    message["To"] = to
    message["Subject"] = subject
    message.attach(MIMEText(f"<html><body>{msg}</body></html>", "html", "utf-8"))

    smtp_client = SMTP(hostname="your-smtp", port=465, use_tls=True)
    async with smtp_client:
        await smtp_client.login(EMAIL, PWD)
        await smtp_client.send_message(message)
