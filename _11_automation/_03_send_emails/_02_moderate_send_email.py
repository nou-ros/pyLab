import os
import smtplib
import imghdr

from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('MY_PASS')

contacts = ['nouros44@gmail.com', 'bazinga_blah@live.com']

# better message pattern 
msg = EmailMessage()
msg['Subject'] = "Check the images"
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'nouros44@gmail.com'

# sending to multiple recepients
# msg['To'] = contacts

# the python documents says to send multiple recepients in comma seperated manner 
# msg['To'] = ', '.join(contacts)

msg.set_content('Attached images...')

'''
# for a single file
with open('cat.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    # print(file_type)
    file_name = f.name 
'''
'''
# for multiple files
files = ['cat.jpg', 'tanjiro.jpg']

for file in files: 
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        # print(file_type)
        file_name = f.name 

    msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)
'''
'''
# for pdf 
files = ['Nouros_CV.pdf']
for file in files: 
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name 

    msg.add_attachment(file_data, maintype="application", subtype='octet-stream', filename=file_name)
'''

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, PASSWORD)
    smtp.send_message(msg)
