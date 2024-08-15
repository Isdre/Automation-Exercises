import json
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import datetime
from email.mime.text import MIMEText

print('Composing Email...')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'isdregg@gmail.com'
TO = 'guszczagilbert@gmail.com'
PASS = ''
with open('pass.json', 'r') as f:
    PASS = json.load(f).get('APP_PASS')

msg = MIMEMultipart()

now = datetime.datetime.now()

msg['Subject'] = f"Top News Stories HN [Automated Email] {now.strftime('%d.%m.%Y')}"
msg['From'] = FROM
msg['To'] = TO

with open("file.txt", "rb") as fil:
    part = MIMEApplication(
        fil.read(),
        Name="file.txt"
    )
# After the file is closed
part['Content-Disposition'] = 'attachment; filename="%s"' % "file.txt"
msg.attach(part)

from web_scaping import extract_news

content = ''

cnt = extract_news('https://news.ycombinator.com')
content += cnt
content += '<br>-------------<br>'
content += '<br><br>\nEnd of Message'

msg.attach(MIMEText(content, 'html'))

print('Initiating SMTP connection...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()

server.login(FROM, PASS)

print('Sending email...')

server.sendmail(FROM, TO, msg.as_string())

print("Email sent!")

server.quit()