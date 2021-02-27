# if two step auth is on we will require app password else we can use the less secure app approach 

import os
import smtplib

# my email and password from enviornment variables.
EMAIL_ADDRESS = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('MY_PASS')

print(EMAIL_ADDRESS, PASSWORD)


# with smtp
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    # identifies us with our mail server which we are using. 
    smtp.ehlo()
    # encrypting our traffic
    smtp.starttls()
    smtp.ehlo()

    # login with our email and password. If there is 2 step auth then app password should be in the password
    smtp.login(EMAIL_ADDRESS, PASSWORD)

    subject = "Greetings!"
    body = 'Hello Nouros!! How are you doing?'

    msg = f'Subject: {subject}\n\n{body}'

    # smtp.sendmail(SENDER, RECIEVER, msg)
    smtp.sendmail(EMAIL_ADDRESS, 'bazinga_blah@live.com', msg)


'''
# with local debuggingserver but first run this command "python -m smtpd -c DebuggingServer -n localhost:1025" in a seperate cmd. with this we will check the email in the debugging server.

with smtplib.SMTP('localhost', 1025) as smtp:
    subject = "Greetings!"
    body = 'Hello Nouros!! How are you doing?'

    msg = f'Subject: {subject}\n\n{body}'

    # # smtp.sendmail(SENDER, RECIEVER, msg)
    smtp.sendmail(EMAIL_ADDRESS, 'bazinga_blah@live.com', msg)
'''