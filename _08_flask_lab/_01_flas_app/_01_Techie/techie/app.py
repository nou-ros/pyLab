from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
# from data import Stories
from functools import wraps
#we installed these
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

ENV = 'dev'

if ENV=='dev':
    app.debug = True
else: 
    app.debug = False


# config MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'techie'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#initialize MYSQL
mysql = MySQL(app)

#to work with static data data.py
# Stories = Stories()

#index
@app.route('/')
def index():
    return render_template('home.html')

#about
@app.route('/about')
def about():
    return render_template('about.html')

#stories
@app.route('/stories')
def stories():
     #create cursor
    cur = mysql.connection.cursor()

    #get stories
    result = cur.execute("SELECT * FROM stories")

    stories = cur.fetchall()

    if result>0:
        return render_template('stories.html', stories = stories)
    else:
        msg = 'No Story Found!'
        return render_template('stories.html', msg=msg)

    #close connection
    cur.close()

#single story
@app.route('/story/<string:id>/')
def story(id):
     #create cursor
    cur = mysql.connection.cursor()

    #get story
    result = cur.execute("SELECT * FROM stories WHERE id = %s", [id])

    story = cur.fetchone()
    return render_template('story.html', story=story)

#register form class
class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

#register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #Create cursor
        cur = mysql.connection.cursor()

        #execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password));

        #commit to DB
        mysql.connection.commit()

        #close connection
        cur.close()
        flash('Thanks for registering with us!', 'success')

        return redirect(url_for('about'))
    return render_template('register.html', form=form)


#user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #get form fileds
        email = request.form['email']
        password_entered = request.form['password']

        #create cursor
        cur = mysql.connection.cursor()

        #get user by email
        result = cur.execute("SELECT * FROM users WHERE email = %s", [email])

        if result > 0:
            #get the stored hash
            data = cur.fetchone() #fetch the first email even if there is many user with same name
            username = data['username']
            password = data['password']

            #compare password
            if sha256_crypt.verify(password_entered, password):
                # app.logger.info('PASSWORD MATCHED')
                # passed
                session['logged_in'] = True
                session['username'] = username
                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))

            else:
                # app.logger.info('PASSWORD DID NOT MATCHED')
                error = 'Invalid login'
                return render_template('login.html', error=error)

                #close connection
                cur.close()
        else:
            error = 'Email not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

#check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

#logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('index'))

#Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    #create cursor
    cur = mysql.connection.cursor()

    #get stories
    result = cur.execute("SELECT * FROM stories")

    stories = cur.fetchall()

    if result>0:
        return render_template('dashboard.html', stories = stories)
    else:
        msg = 'No Story Found!'
        return render_template('dashboard.html', msg = msg)

    #close connection
    cur.close()

#Story From class
class StoryForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])
    
#Add Story
@app.route('/add_story', methods=['GET', 'POST'])
@is_logged_in
def add_story():
    form = StoryForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        #create cursor
        cur = mysql.connection.cursor()

        #execute
        cur.execute("INSERT INTO stories(title, body, author) VALUES(%s, %s, %s)", (title, body, session['username']))

        #commit to DB
        mysql.connection.commit()

        #close connection
        cur.close()

        flash('Story Created', 'success')

        return redirect(url_for('dashboard'))
    
    return render_template('add_story.html', form=form)



#Edit Story
@app.route('/edit_story/<string:id>/', methods=['GET', 'POST'])
@is_logged_in
def edit_story(id):
    #create cursor
    cur = mysql.connection.cursor()

    #get story by id
    result = cur.execute("SELECT * FROM stories WHERE id = %s", [id])

    story = cur.fetchone()

    #get form
    form = StoryForm(request.form)

    #populate story from fields 
    form.title.data = story['title']
    form.body.data = story['body']

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']

        #create cursor
        cur = mysql.connection.cursor()

        #execute
        cur.execute("UPDATE stories SET title=%s, body=%s WHERE id = %s", (title, body, id))

        #commit to DB
        mysql.connection.commit()

        #close connection
        cur.close()

        flash('Story Updated', 'success')

        return redirect(url_for('dashboard'))
    
    return render_template('edit_story.html', form=form)


#delete story
@app.route('/delete_story/<string:id>/', methods=['POST'])
@is_logged_in
def delete_story(id):
    #create cursor
    cur = mysql.connection.cursor()

    #execute
    cur.execute("DELETE FROM stories WHERE id = %s", [id])

    #commit to DB
    mysql.connection.commit()

    #close connection
    cur.close()

    flash('Story Deleted', 'success')
    
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    #session starting for registration
    app.secret_key='secret123'
    app.run()