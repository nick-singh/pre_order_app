from sqlalchemy import String, create_engine, ForeignKey, Sequence,  text, TIMESTAMP
import traceback
from app import db


tablename = 'mobile_plan'

class MobilePlans(db.Model):
    """docstring for MobilePlans"""
    __tablename__ = tablename
    id = db.Column(db.Integer, Sequence('mobileplan_seq'), primary_key=True)
    name = db.Column(db.String(250))
    sms = db.Column(db.String(250))
    data = db.Column(db.String(250))
    voice = db.Column(db.String(250))
    price = db.Column(db.String(250))