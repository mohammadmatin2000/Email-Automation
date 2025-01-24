import smtplib
import ssl
from credentials import password
from email.message import EmailMessage
# ======================================================================================================================
sender="Sender email"
recipient="Recipient email"
title="Openweathermap service "
body="Explanation about Openweathermapservice api"
# ======================================================================================================================
email=EmailMessage()
email['from']=sender
email['to']=recipient
email['subject']=title
email.set_content(body)
# ======================================================================================================================
with open("OpenWeatherMap service.docx","rb") as fill:
    email.add_attachment(fill.read(),maintype="docx",subtype="docx",filename=fill.name)
# ======================================================================================================================
num=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=num) as fill_1:
    fill_1.login(sender,password)
    fill_1.send_message(email)
    print("OK")
# ======================================================================================================================