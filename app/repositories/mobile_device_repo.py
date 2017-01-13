from app import db
from app.models.mobile_devices import MobileDevices
from app.modules.utils import obj_to_dict
from sqlalchemy import func
import traceback
import hashlib

class MobileDevicesRepo(object):
	"""docstring for MobileDevicesRepo"""
	
	def add(self, device):
		print device
		u = devices(**device['device'])
		try:
			db.session.add(u)
			db.session.commit()
			db.session.expire_all()
			return obj_to_dict(u)
		except Exception, e:
			print traceback.format_exc()
			return None


	def remove(self, deviceid):
		try:
			db.session.query(MobileDevices).filter(MobileDevices.id == deviceid).delete(synchronize_session='fetch')
			db.session.commit()
			return True
		except Exception, e:
			print traceback.format_exc()
			return False

	def update(self, id, data):
		try:
			device = db.session.query(MobileDevices).filter(MobileDevices.id == id).update(data)
			db.session.commit()
			return obj_to_dict(device)
		except Exception, e:
			print traceback.format_exc()
			return None

	def get_all(self):
		try:
			devices = db.session.query(MobileDevices).all()
			devices = [obj_to_dict(c) for c in devices]
			return devices
		except Exception, e:
			print traceback.format_exc()
			return None

	def get_device_by_id(self, id):
		try:
			device = db.session.query(MobileDevices).\
			filter(MobileDevices.id == id).first()
			return obj_to_dict(device)
		except Exception, e:
			print traceback.format_exc()
			return None		
