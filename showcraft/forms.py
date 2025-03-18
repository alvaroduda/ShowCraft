from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class CadastroForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    confirmar_senha = PasswordField('Confirme a senha', validators=[DataRequired(), EqualTo('senha')])
    submit = SubmitField('Cadastrar')

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(min=3, max=20)])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')
