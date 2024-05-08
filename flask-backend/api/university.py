from flask import jsonify, request
from sqlalchemy import exc
from flask_sqlalchemy import session,query
from models import *
from api.cors import corsify_actual_response

def add_uni():
    result = {}
    name = request.form.get("role")
    if name is None:
        result['status'] = 'error occured'
        result['error'] = 'no username'
        return corsify_actual_response(jsonify(result))

	
    new_uni = University()
    new_uni.name = name

    if new_uni:
        try:
            db.session.add(new_uni)
            db.session.commit()
        #Проблемы с добавлением - пишем об этом
        except exc.SQLAlchemyError as e:
            result['error'] = 'SQL error'
            success = False


    return corsify_actual_response(jsonify(result))



def get_uni():
	result = {}
	name = request.form.get("university")
	if not name is None:
		unis = University.query.filter(University.name == name).all()
	unis = University.query.all()

	for i in range(len(unis)):
		result[i] = unis[i].format()
	return corsify_actual_response(jsonify(result))

