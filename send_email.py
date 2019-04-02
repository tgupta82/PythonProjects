import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
msg['From'] = 'tanuj.gupta82@gmail.com'
msg['To'] = 'deeptipresent@gmail.com'
msg['Subject'] = 'Love Message!'
body = 'I love you Deepti...'

msg.attach(MIMEText(body, 'plain'))

filename = 'C:/Users/tanuj/MyProjects/PythonLearning/Sample/Document.txt'
attachment = open(filename, 'rb')

# Allowing the upload the attachment
part = MIMEBase('application', "octet-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-attached', "attachment: filename = " + filename)

msg.attach(part)
text = msg.as_string()

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('tanuj.gupta82@gmail.com', 'Panipat@311')
mail.sendmail('tanuj.gupta82@gmail.com', 'deeptipresent@gmail.com', text)
mail.close()
