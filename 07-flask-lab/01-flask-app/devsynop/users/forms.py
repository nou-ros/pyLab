from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from devsynop.models import User
from flask_login import current_user
#for image update
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')
    
    #checking in form if a field already exists before checking with models
    def validate_username(self, username):
        # username.data comes from the form
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Username already exists.')

    def validate_email(self, email):
        # email.data comes from the form
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email already taken.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    avatar = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
    
    #checking in form if a field already exists before checking with models
    def validate_username(self, username):
        if username.data != current_user.username: 
            # username.data comes from the form
            user = User.query.filter_by(username=username.data).first()

            if user:
                raise ValidationError('Username already exists.')

    def validate_email(self, email):
        if email.data != current_user.email: 
            # email.data comes from the form
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Email already taken.')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])

    submit = SubmitField('Change password')

    def validate_email(self, email):
        # email.data comes from the form
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('User with this email does not exist. Please register first!')

class ResetPassowrdForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
