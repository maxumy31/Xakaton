from flask import jsonify, request
from sqlalchemy import exc
from flask_sqlalchemy import session,query
from models import *

#ПОСТ запрос, вход
def add_role():
	result = {}
	name = request.form.get("role")

	if name is None:
		result['status'] = 'error occured'
		result['error'] = 'no username'
		return jsonify(result)
	
	new_role = Roles()
	new_role.name = name

	if new_role:
		try:
			db.session.add(new_role)
			db.session.commit()
		#Проблемы с добавлением - пишем об этом
		except exc.SQLAlchemyError as e:
			result['error'] = 'SQL error'
			success = False


	return jsonify(result)


def get_role():
	result = {}


	name = request.form.get("role")


	if not name is None:
		roles = Roles.query.filter(Roles.name == name).all()
	roles = Roles.query.all()

	for i in range(len(roles)):
		result[i] = roles[i].format()
	return jsonify(result)

