from app import db
from app.models.orders import Orders
from app.modules.utils import obj_to_dict
from sqlalchemy import func
import traceback
import hashlib

class OrdersRepo(object):
	"""docstring for OrdersRepo"""
	
	def add(self, order):
		print order
		u = orders(**order['order'])
		try:
			db.session.add(u)
			db.session.commit()
			db.session.expire_all()
			return obj_to_dict(u)
		except Exception, e:
			print traceback.format_exc()
			return None


	def remove(self, orderid):
		try:
			db.session.query(Orders).filter(Orders.id == orderid).delete(synchronize_session='fetch')
			db.session.commit()
			return True
		except Exception, e:
			print traceback.format_exc()
			return False

	def update(self, id, data):
		try:
			order = db.session.query(Orders).filter(Orders.id == id).update(data)
			db.session.commit()
			return obj_to_dict(order)
		except Exception, e:
			print traceback.format_exc()
			return None

	def get_all(self):
		try:
			orders = db.session.query(Orders).all()
			orders = [obj_to_dict(c) for c in orders]
			return orders
		except Exception, e:
			print traceback.format_exc()
			return None

	def get_order_by_id(self, id):
		try:
			order = db.session.query(Orders).\
			filter(Orders.id == id).first()
			return obj_to_dict(order)
		except Exception, e:
			print traceback.format_exc()
			return None		
