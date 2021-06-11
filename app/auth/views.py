from flask import render_template, request, redirect, url_for
from wtforms import form
from flask_login import login_user, login_required, logout_user
from . import auth
from app.models import user

@auth.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method : 'POST'
   return render_template('login.html')
   form = request.form
   username = form.get('username')
   password = form.get('password')
   print(username)
       