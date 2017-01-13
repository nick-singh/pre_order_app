from sqlalchemy import String, create_engine, ForeignKey, Sequence,  text, TIMESTAMP
import traceback
from app import db


tablename = 'orders'

class Orders(db.Model):
	"""docstring for Orders"""
	__tablename__ = tablename
	id = db.Column(db.Integer, Sequence('orders_seq'), primary_key=True)
	client_id = db.Column(db.Integer, ForeignKey('clients.id'))
	mobileplan_id = db.Column(db.Integer, ForeignKey('mobile_plan.id'))
	deviceid = db.Column(db.Integer, ForeignKey('mobile_devices.id'))
	pick_up_location = db.Column(db.String(250))
	timestamp = db.Column(db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))