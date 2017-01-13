from app import db
from app.models.mobile_plan import MobilePlans
from app.modules.utils import obj_to_dict
from sqlalchemy import func
import traceback
import hashlib

class MobilePlansRepo(object):
	"""docstring for MobilePlansRepo"""
	
	def add(self, plan):
		print plan
		u = plans(**plan['plan'])
		try:
			db.session.add(u)
			db.session.commit()
			db.session.expire_all()
			return obj_to_dict(u)
		except Exception, e:
			print traceback.format_exc()
			return None


	def remove(self, planid):
		try:
			db.session.query(MobilePlans).filter(MobilePlans.id == planid).delete(synchronize_session='fetch')
			db.session.commit()
			return True
		except Exception, e:
			print traceback.format_exc()
			return False

	def update(self, id, data):
		try:
			plan = db.session.query(MobilePlans).filter(MobilePlans.id == id).update(data)
			db.session.commit()
			return obj_to_dict(plan)
		except Exception, e:
			print traceback.format_exc()
			return None

	def get_all(self):
		try:
			plans = db.session.query(MobilePlans).all()
			plans = [obj_to_dict(c) for c in plans]
			return plans
		except Exception, e:
			print traceback.format_exc()
			return None

	def get_plan_by_id(self, id):
		try:
			plan = db.session.query(MobilePlans).\
			filter(MobilePlans.id == id).first()
			return obj_to_dict(plan)
		except Exception, e:
			print traceback.format_exc()
			return None		
