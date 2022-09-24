from .Base import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):

    serialize_only = ('name', 'email')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(80))