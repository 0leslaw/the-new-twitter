from flask import Flask
# Things to import at the beginning
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager


# Declarations to insert before the create_app function:
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


def create_app(test_config=None):
    app = Flask(__name__)

    # A secret for signing session cookies
    app.config["SECRET_KEY"] = "93220d9b340cf9a6c39bac99cce7daf220167498f91fa"
    
    app.config[
    "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+pymysql://microblog:waDBlog@localhost/Microblog"
    
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)  # Initialize the LoginManager with the app

    # Register blueprints
    # (we import main from here to avoid circular imports in the next lab)
    from . import model
    @login_manager.user_loader
    def load_user(user_id):
      return db.session.get(model.User, int(user_id))
    
    from . import main
    from . import auth
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    return app
  

