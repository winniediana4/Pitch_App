from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
  __tablename__ ='users'
  id = db.Column(db.Integer, primary_key=True)