import os
import smtplib

from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('MY_PASS')

msg = EmailMessage()
msg['Subject'] = "Check the images"
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'nouros44@gmail.com'

msg.set_content('Attached html')

msg.add_alternative('''\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML EMAIL</title>
</head>
<body>
    <h1 style="color:slateblue;">This is a HTML Email!</h1>
</body>
</html>
''', subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, PASSWORD)
    smtp.send_message(msg)
