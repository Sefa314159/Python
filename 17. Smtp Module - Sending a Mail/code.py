import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

message             = MIMEMultipart()

message["From"]     = "asdfdsf@gmail.com"

message["To"]       = "send@gmail.com"

message["Subject"]  = "Smtp type sending Mail"

writing             = """

Hello sending mail with Python World !

Sefa Isci

"""

message_body = MIMEText(writing, "plain")

message.attach(message_body)

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    
    mail.ehlo()
    
    mail.starttls()
    
    mail.login("asdfdsf", "asdfdsf") # mail.login(username, password)
    
    mail.sendmail(message["From"], message["To"], message.as_string())
    
    mail("Mail sent successfully...")
    
    mail.close()
    
except:
    sys.stderr.write("A problem occurred!")
    sys.stderr.flush()
