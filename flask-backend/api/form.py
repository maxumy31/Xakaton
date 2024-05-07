from flask import jsonify, request
from sqlalchemy import exc
from flask_sqlalchemy import session,query
from models import *



def get_form_by_id():
	result = {}
	id = request.args.get("form_id")
	form = None
	if id is None:
		result['status'] = 'error occured'
		result['error'] = 'not enough arguments'
	else:
		form = Form.query.filter(Form.id == id).first()
		result['data'] = form.format()
		result['status'] = 'completed'

	return result



def get_all_forms():
	result = {}
	forms = None

	forms = Form.query.all()
	result['data'] = {}
	niger = 0
	for i in forms:
		result['data'][niger] = i.format()
		niger = niger + 1

	result['status'] = 'completed'
	return result

	

