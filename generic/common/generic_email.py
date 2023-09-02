import os
import configparser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

config = configparser.ConfigParser()
config.read(r"D:\datalake\ingestion\onetoone\configfiles\email_config.ini")
sender_email = config.get('email_details', 'sender_email')
receiver_email = config.get('email_details', 'receiver_email')
subject = config.get('email_details', 'subject')

message = """
Hi team,
File issue with delimeter.Please check and resolve

Thanks,
Anil Challa
"""



config = configparser.RawConfigParser()
config.read(r"D:\datalake\ingestion\onetoone\configfiles\email_config.ini")
config.set('email_details','message_email',message)
print("config message to set")


username = os.getenv('gmail_user')
password = os.getenv('gmail_password')

# Create a MIME multipart message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject



# Attach the message to the MIME message
msg.attach(MIMEText(message, 'plain'))

# SMTP server and port for Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 465


# Create a secure SSL/TLS connection
context = smtplib.SMTP_SSL(smtp_server, smtp_port)

# Uncomment the following line if you're using a non-SSL SMTP server (e.g., Outlook)
# context = smtplib.SMTP(smtp_server, smtp_port)

# Login to the email account
context.login(username, password)

# Send the email
context.sendmail(sender_email, receiver_email, msg.as_string())

# Close the connection
context.quit()

print("message send")



