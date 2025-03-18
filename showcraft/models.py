from showcraft import db, login_manager
from flask_login import UserMixin
from datetime import datetime

# Carregamento do usuário para o sistema de login
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    senha = db.Column(db.String(256), nullable=False)
    texturas = db.relationship("Textura", backref="usuario", lazy=True)  

class Textura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    textura = db.Column(db.String(150), default="default.rar")
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
