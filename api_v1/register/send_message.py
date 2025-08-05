import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_message(email: str, code: str):
    addr_from = "hwappinfo@gmail.com"
    addr_to = email
    password = "fmgjybogrljzdtgl"

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = 'Регистрация hwApp'

    body = f"Ваш код для регестрации: {code}"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()
