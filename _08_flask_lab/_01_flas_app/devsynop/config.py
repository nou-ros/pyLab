import os

class Config:
    # secret key is used to sign session cookies for protection against cookie data tampering for form data 
    SECRET_KEY = ''
    # configuring sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME = os.environ.get('MY_EMAIL')
    MAIL_PASSWORD = os.environ.get('MY_PASS')