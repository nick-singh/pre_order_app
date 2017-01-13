from sqlalchemy import String, create_engine, ForeignKey, Sequence,  text, TIMESTAMP
import traceback
from app import db


tablename = 'clients'

class Clients(db.Model):
    """docstring for Clients"""
    __tablename__ = tablename
    id = db.Column(db.Integer, Sequence('client_seq'), primary_key=True)
    username = db.Column(db.String(250))
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    email = db.Column(db.String(250))
    address = db.Column(db.String(250))
    password = db.Column(db.String(250))
    timestamp = db.Column(db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))