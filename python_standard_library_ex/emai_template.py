from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
# we need to import the module Template
from string import Template
import smtplib
# Using the module Template we are going to read the HTML file
template = Template(Path("template.html").read_text())
message = MIMEMultipart()
message["from"] = "Yuri Avello"
message["to"] = "RECEIVER@gmail.com"
message["subject"] = "This is a test"
# With substitute we can indicate what to put instead of $name
body = template.substitute({"name": "john"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("game2.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("SENDER@gmail.com", "PASSWORD")
    smtp.send_message(message)
print("sent...")
