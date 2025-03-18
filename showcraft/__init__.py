from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

# Inicializando a aplicação
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))

# Configuração da aplicação
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ShowCraft.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '4297e4ecdfe050ce15463fa0389c098b537865259d485df4401aa767e5bc2914'

# Inicializando extensões
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"  


from showcraft import models, routes