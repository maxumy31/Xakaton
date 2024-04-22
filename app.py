from flask import Flask,render_template,jsonify,request
from flask_migrate import Migrate
from models import *
from api.user import *

#Запускаем фласк, templates - папка шаблонов
app = Flask(__name__,template_folder='templates')

#Указываем путь к БД для SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:JDH@localhost:5432/data"

#Отключить уведомления об операциях(хз как работает)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Хватаем БД из файла models и инициализируем нашим приложением
db.init_app(app)

#Мигрирование БД
migrate = Migrate(app,db)



#Подключение API для user
app.add_url_rule("/user",view_func=get_user,methods = ["GET"])
app.add_url_rule("/user/username",view_func=get_user_by_username,methods = ["GET"])
app.add_url_rule("/user/login",view_func=login,methods = ["POST"])

app.add_url_rule("/user",view_func=create_user,methods = ["POST"])
app.add_url_rule("/user",view_func=update_user,methods = ["PUT"])
app.add_url_rule("/user",view_func=delete_user,methods = ["DELETE"])

#Главная страница
@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template("index.html",name = ", niger")

#Запуск
if __name__ == '__main__':
	app.run(debug=True)