import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
msg = EmailMessage()
msg['From'] = "Me"
msg['To'] = "You"
msg['Subject'] = "You won 1,000,000,000 $!!!!"#Example of subject, also you can costumise it.

msg.set_content(html.substitute({"name": "Tintin"}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("put your email adress here", "put your password here")
    smtp.send_message(msg)
    print("All good boss!!!!!!!!")