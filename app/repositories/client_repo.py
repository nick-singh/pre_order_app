from app import db
from app.models.clients import Clients
from app.modules.utils import obj_to_dict
from sqlalchemy import func
import traceback
import hashlib


class Client_Repository(object):
	"""docstring for Client_Repository"""

	def add(self, client):
		print client
		u = clients(**client['client'])
		try:
			db.session.add(u)
			db.session.commit()
			db.session.expire_all()
			return obj_to_dict(u)
		except Exception, e:
			print traceback.format_exc()
			return None


	def remove(self, clientid):
		try:
			db.session.query(Clients).filter(Clients.id == clientid).delete(synchronize_session='fetch')
			db.session.commit()
			return True
		except Exception, e:
			print traceback.format_exc()
			return False

	def update(self, id, data):
		try:
			client = db.session.query(Clients).filter(Clients.id == id).update(data)
			db.session.commit()
			return obj_to_dict(client)
		except Exception, e:
			print traceback.format_exc()
			return None

	def get_all(self):
		try:
			clients = db.session.query(Clients).all()
			clients = [obj_to_dict(c) for c in clients]
			return clients
		except Exception, e:
			print traceback.format_exc()
			return None

	def get_client_by_id(self, id):
		try:
			client = db.session.query(Clients).\
			filter(Clients.id == id).first()
			return obj_to_dict(client)
		except Exception, e:
			print traceback.format_exc()
			return None