from flask import Flask,render_template,jsonify,request
from flask_migrate import Migrate
from models import *



#Запускаем фласк, templates - папка шаблонов
app = Flask(__name__,template_folder='templates')

#Указываем путь к БД для SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:JDH@localhost:5432/data"

#Хватаем БД из файла models и инициализируем нашим приложением
db.init_app(app)

#Мигрирование БД
migrate = Migrate(app,db)

#Тестировал работу АПИ
@app.get('/API')
def get_users():
	users = User.query.all()
	name = request.args.get("name") 
	if not name:
		return jsonify({"status":"error"})
	data = {'info': name}
	return jsonify(data)

#Главная страница
@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template("index.html",name = ", niger")

#Запуск
if __name__ == '__main__':
	app.run(debug=True)