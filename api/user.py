from flask import jsonify, request
from sqlalchemy import exc
from flask_sqlalchemy import session,query
from models import *

#ПОСТ запрос, вход
def login():
	result = {}
	name = request.form.get("username")
	pswd = request.form.get("password")

	if pswd is None:
		result['status'] = 'error occured'
		result['error'] = 'no password'
		return jsonify(result)

	if name is None:
		result['status'] = 'error occured'
		result['error'] = 'no username'
		return jsonify(result)
	

	user = User.query.filter(User.username == name).first()
	
	if(bcrypt.check_password_hash(user.password,pswd)):
		result['status'] = 'completed'
		result['user'] = user.format()
	else:
		result['status'] = 'error occured'
		result['error'] = 'wrong password'

	return jsonify(result)

#ГЕТ запрос, НЕДОДЕЛАН
def get_user():
	result = {}


	name = request.form.get("username")
	pswd = request.form.get("password")
	unversity_id = request.form.get("university_id")
	role_id = request.form.get("role_id")

	if not name is None:
		users = User.query.filter(User.username == name).all()
	users = User.query.all()

	for i in range(len(users)):
		result[i] = users[i].format()
	return jsonify(result)

#ГЕТ запрос по username
def get_user_by_username():
	result = {}

	name = request.args.get("username")
	print(name)

	if not name is None:
		users = User.query.filter(User.username == name).first()
		result['status'] = 'completed'
		result['user'] = users.format()
	else:
		result['status'] = 'error occured'
		result['error'] = 'user not found'

	
	return jsonify(result)

#ПОСТ запрос 
def create_user():
	result = {}
	success = True
	can_be_constructed = True
	name = request.form.get("username")
	pswd = request.form.get("password")
	unversity_id = request.form.get("university_id")
	role_id = request.form.get("role_id")

	print(name,pswd,unversity_id,role_id)
	#Что то не введено -  объект не собрать
	if name is None or pswd is None or unversity_id is None or role_id is None:
		result['error'] = 'not enough data'
		success = False
		can_be_constructed = False

	new_user = None
	#Объект не собрать - пытаемся
	if(can_be_constructed):
		new_user = User(name,pswd)
		new_user.university_id = unversity_id
		new_user.role = role_id

	#Объект не собран - говорим что ошибка
	if not new_user:
		success = False

	#Пробуем добавить в БД только если объект существует
	if new_user:
		try:
			db.session.add(new_user)
			db.session.commit()
		#Проблемы с добавлением - пишем об этом
		except exc.SQLAlchemyError as e:
			result['error'] = 'SQL error'
			success = False

	if success:
		result['status'] = 'completed'
	else:
		result['status'] = 'error occured'

	return jsonify(result)


def update_user():
		return jsonify({'Method':"PUT"})


def delete_user():
		return jsonify({'Method':"DELETE"})
