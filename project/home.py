from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user

home = Blueprint('home', __name__)

@home.route('/')
def index():
  return render_template('index.html')

@home.route('/profile')
@login_required
def profile():
  return render_template('profile.html', name=current_user.name)

@home.route('/jello')
def jello():
  return 'jello'

@home.route('/objects')
def objects():
    n = [{"id": 1, "name": "bob"}, {"id": 2, "name": "joe"}]
    return jsonify(n)

