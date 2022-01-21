import secrets
import os
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from devsynop import mail

def save_picture(form_picture):
    # provide random name
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_filename)

    # resizing the image
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_filename

def send_reset_email(user):
    token = user.get_reset_token()
    msg=Message('Password Reset Request', 
                sender="noreply@demo.com", 
                recipients=[user.email])
    msg.body = f'''
    To reset your password, visit the following link: {url_for('reset_token', token=token, _external=True)}

    If you did not make this request then simple ignore the mail.
    '''
    mail.send(msg)

