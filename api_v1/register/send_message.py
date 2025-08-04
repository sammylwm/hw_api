import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_message():
    addr_from = "hwappinfo@gmail.com"
    addr_to = "hopemikaelsonl@yandex.ru"
    password = "fmgjybogrljzdtgl"

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = 'Тема сообщения'

    body = "Текст сообщения"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()

send_message()