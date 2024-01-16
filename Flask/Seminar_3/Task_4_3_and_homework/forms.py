from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from werkzeug.security import generate_password_hash, check_password_hash


class RegisterForm(FlaskForm):
    """
    Форма регистрации
    """

    first_name = StringField(name="first_name")
    last_name = StringField(name="last_name")
    email = EmailField(name="email")
    password = PasswordField(name="password1")
    passsword_2 = PasswordField(name="password2")


class LoginForm(FlaskForm):
    """
    Форма логина
    """
    email = EmailField(name="email")
    password = PasswordField(name="password")
    
        
