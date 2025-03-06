"""<<< Importações >>>"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_required
from flask_bcrypt import Bcrypt


"""<<< Importações >>>"""




"""<<< Criações >>>"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ShowCraft.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '9c3e6c929cb1e8197d5887ff5bdf47f8'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

"""<<< Criações >>>"""




"""<<< Rotas >>>"""

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home1():
    return render_template('home.html')

@app.route('/perfil/<user>')
@login_required
def perfil(user):
    return render_template('perfil.html', user=user)

"""<<< Rotas >>>"""




"""<<< Classes >>>"""

@login_manager.user_loader
def load_usuario (id):
    return Usuario.query.get(int(id))

class Usuario(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    senha = db.Column(db.String, nullable=False)
    txt = db.relationship("Textura", backref="usuario", lazy=True)

class Textura(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    textura = db.Column(db.String, default="default.rar")
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

"""<<< Classes >>>"""




"""<<< Main >>>"""

if __name__ == "__main__":
    app.run(debug=True)

"""<<< Main >>>"""