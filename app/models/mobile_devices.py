from sqlalchemy import String, create_engine, ForeignKey, Sequence,  text, TIMESTAMP
import traceback
from app import db


tablename = 'mobile_devices'

class MobileDevices(db.Model):
    """docstring for MobileDevices"""
    __tablename__ = tablename
    id = db.Column(db.Integer, Sequence('mobiledevices_seq'), primary_key=True)
    name = db.Column(db.String(250))
    price = db.Column(db.String(250))