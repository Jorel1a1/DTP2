from app import db
from app import login
from datetime import datetime 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


association_table = db.Table('association', 
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    
)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(UserMixin, db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return f'<User {self.username:}>'





#db.create_all()
