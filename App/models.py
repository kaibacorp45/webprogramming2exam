from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import check_password_hash, generate_password_hash


db = SQLAlchemy()

def get_migrate(app):
    return Migrate(app, db)

def create_db(app):
    db.init_app(app)
    db.create_all(app=app)
    
def init_db(app):
    db.init_app(app)

# models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def toDict(self):
        return{
          'id': self.id,
          'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

#review

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text =  db.Column(db.String(500), nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    isbn = db.Column(db.String(120), db.ForeignKey('book.isbn'), nullable = False)

    def toDict(self):
        return{
          'text': self.text,
          'rating': self.rating
      #add isbn maybe
        }

class Book(db.Model):
    isbn = db.Column(db.String(120), primary_key=True)
    title =  db.Column(db.String(120), nullable=True)
    author = db.Column(db.String(120), nullable=True)
    publication_year = db.Column(db.Integer, nullable = True)
    publisher =  db.Column(db.String(120), nullable=True)
    review = db.relationship('Review', backref='book', lazy=True,cascade="all, delete-orphan")

    def toDict(self):
        return{
          'isbn': self.isbn,
          'title': self.title,
          'author': self.author,
          'publication_year': self.publication_year,
          'publisher': self.publisher,
      #add isbn maybe
        }

    def get_avg_rating(self):
      avg = 0
      sum = 0
      for r in review:
        sum = sum + review.rating
        count = count + 1
      avg = sum/count
      return avg


   