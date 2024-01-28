from os import linesep
from flask import Blueprint, render_template, request, url_for, redirect, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import _db


auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
  return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
  name = request.form.get('name')
  email = request.form.get('email')
  password = request.form.get('password')

  user = User.query.filter_by(email=email).first()
  if user:
    return redirect(url_for('auth.signup'))

  new_user = User(name=name, email=email, password=generate_password_hash(password))
  _db.session.add(new_user)
  _db.session.commit()
  print("names in table user:")
  n = User.query.all()
  for i in n:
    print(i.name)
  
  return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
  return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
  email = request.form.get('email')
  password = request.form.get('password')
  print(email,password)
  '''remember = True if request.form.get("remember") else False

  user = User.query.filter_by(email=email).first()
  if not user or not check_password_hash(user.password, password):
    return redirect(url_for('auth.login'))

  login_user(user, remember=remember)'''
  
  return redirect(url_for('home.profile'))


@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect('home.index')







