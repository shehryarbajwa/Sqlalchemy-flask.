from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://shehryarbajwa@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
  #Two attributes within the Person Model. One is the id, the other is the name
  #The name of the table is persons
  #The name of the first column is id which contains integers and has a primary key
  #The name of second column is the name which contains a string and is not null
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)

db.create_all()

@app.route('/')
def index():
  person = Person.query.first()
  return 'Hello ' + person.name