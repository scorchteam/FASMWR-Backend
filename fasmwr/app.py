from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import BaseConfig
import os

# Flask App
app = Flask(__name__)
CORS(app, support_credentials=True)

# Database
db = SQLAlchemy()
bcrypt = Bcrypt()

app.config.from_object(BaseConfig)
db.app = app
app.app_context().push()
db.init_app(app)
bcrypt.init_app(app)


# Routing
from routes.routes import fasmwr
from routes.user import users

app.register_blueprint(fasmwr)
app.register_blueprint(users)


if __name__ == '__main__':
    app.run()