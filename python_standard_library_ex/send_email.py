# email is a package, mime is a subpackage, Multipurpose Internet Mail Extension
# is a standar to define the format of email
# multipart is another package that contain the module MIMEMultipart
#  with it we can send email that contains HTML and plain text content
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage  # to send image
# we need this module to give the SMTP to send email
import smtplib
from pathlib import Path
message = MIMEMultipart()
# those are heading allowed by the module
message["from"] = "NAME LASTNAME"
message["to"] = "RECEIVER@gmail.com"
message["subject"] = "This is a test"
# there is not one for the body of the email so we need to use the 'attach', that require a paylond as argument
# payload can be text, image ...
# if we do not specify it will send plain text, if we want we can add "HTML" to specify it
message.attach(MIMEText("Body"))
# to send an image
message.attach(MIMEImage(Path("game2.jpg").read_bytes()))
# the first key argument specify the SMTP service, the second the port
#smtplib.SMTP(host="smtp.gmail.com", port=587)
# after that we need to close it to release the resources
# smtp.close()
# as we see before we can use with
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # with this we say to server 'hey, i am a client and ready!
    smtp.starttls()  # put the SMTP server in tls mode: Transport Layer Security, so we send encrypted instruction
    smtp.login("SENDER@gmail.com", "PASSWORD")
    smtp.send_message(message)
print("sent...")
