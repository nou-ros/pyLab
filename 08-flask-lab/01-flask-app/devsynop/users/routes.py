from flask import render_template, url_for, flash, redirect, request, abort, Blueprint

from devsynop.users.forms import (RegistrationForm, LoginForm, UpdateProfileForm, 
                   RequestResetForm, ResetPassowrdForm)
from devsynop import db, bcrypt
from devsynop.models import User, Post
# flask auth functionality
from flask_login import login_user, current_user, logout_user, login_required
from devsynop.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # hashing the password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # setting the data in user table
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # adding the user in the session
        db.session.add(user)
        # saving the user in database
        db.session.commit()
        flash(f'Your account has been created! Please login to continue', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html', title="Register", form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    # if already logged in then redirect to index page
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # login using flasklogin extension
            login_user(user, remember=form.remember.data)
            # getting the pattern from url [this will allow us to go to our profile directly if we use the url pattern before logging in.]
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect (url_for('main.index'))
        else:
            flash(f'Login in failed! Please check your email and password again.', 'danger')
    return render_template('login.html', title="Login", form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@users.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        # updating images
        if form.avatar.data: 
            picture_file = save_picture(form.avatar.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data 
        current_user.email = form.email.data
        db.session.commit()
        flash('Profile information has been updated!', 'success')
        return redirect(url_for('users.profile'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('profile.html', title="Profile", image_file=image_file, form=form)


# user specific posts 
@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        #sending token to the email
        send_reset_email(user)
        flash('An email has been sent to reset your password', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('Token has expired', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPassowrdForm()

    if form.validate_on_submit():
        # hashing the password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        # saving the user in database
        db.session.commit()
        flash(f'Your pasword has been updated! Please login to continue', 'success')
        return redirect(url_for('users.login'))

    return render_template('reset_token.html', title='Reset Token', form=form)