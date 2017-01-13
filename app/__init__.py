from flask import Flask, request, session, redirect, send_file, jsonify
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__, instance_relative_config=True, static_url_path="")

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


from app.models.clients import Clients
from app.models.mobile_devices import MobileDevices
from app.models.mobile_plan import MobilePlans
from app.models.orders import Orders

from app.modules.utils import format_jsend_response
from app.modules.utils import authenticate, deauthenticate, requires_auth

from app.repositories.client_repo import Client_Repository

client_repo = Client_Repository()

@app.route('/')
def root(): 
  return app.send_static_file('index.html')



@app.route('/clients', methods=['GET', 'POST'])
# @requires_auth('client')
def all_clients_handler():
	if request.method == 'GET':	
		data = client_repo.get_all()
		if data is None:
			return format_jsend_response(status="error", message="There was an error getting all Clients")
		return format_jsend_response(status="success", data=data)
	if request.method == 'POST':
		data = request.json['data']
		client = client_repo.add(data)
		if client is None:
			return format_jsend_response(status="error", message="There was an error adding the client")
		return format_jsend_response(status="success", data=client)


@app.route('/client/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@requires_auth('client')
def client_handler(id):
	if request.method == 'GET':
		client = client_repo.get_client_by_id(id)
		if client is None:
			return format_jsend_response(status="error", message="There was an error getting client with id %s"%id)
		return format_jsend_response(status="success", data=client)
	if request.method == 'PUT':
		data = request.json['data']
		client = client_repo.update(id, data)
		if client is None:
			return format_jsend_response(status="error", message="There was an error updating client %s"%id)
		return format_jsend_response(status="success", data=client)
	if request.method == 'DELETE':
		deleted = client_repo.remove(id)
		if not deleted:
			return format_jsend_response(status="error", message="There was an error deleting client %s" %id)
		return format_jsend_response(status="success", data={"id":id})