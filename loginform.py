from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_ast = StringField('id астронавта', validators=[DataRequired()])
    id_cap = StringField('id капитана', validators=[DataRequired()])
    password_ast = PasswordField('Пароль астронавта', validators=[DataRequired()])
    password_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')