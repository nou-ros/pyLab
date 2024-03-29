
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from flask_login import LoginManager

# install the package
from flask_mail import Mail

from devsynop.config import Config


# database instance 
db = SQLAlchemy()

bcrypt = Bcrypt()

login_manager = LoginManager()
# with this if we go to accunt url without logging in it will redirect to login url
login_manager.login_view = 'users.login'

login_manager.login_message_category = 'info'

mail = Mail()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from devsynop.users.routes import users
    from devsynop.stories.routes import stories
    from devsynop.main.routes import main
    from devsynop.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(stories)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    
    return app