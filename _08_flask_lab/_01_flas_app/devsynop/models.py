# separating models in a different file
from datetime import datetime
from devsynop import db, login_manager
from flask_login import UserMixin
from flask import current_app
# for token 
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# user model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # nullable - field cann't be empty
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # String will be hashed with 20 chars
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    # String will be hashed with 60 chars
    password = db.Column(db.String(60), nullable=False)

    # backref - will refer to the user via author field from post model
    # lazy - load the data as necessary in one go.
    posts = db.relationship('Post', backref='author', lazy=True)


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try: 
            user_id = s.loads(token)['user_id']
        except: 
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# post Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

    def __repr__(self):
        return f"Post ('{self.title}', '{self.date_posted}')"