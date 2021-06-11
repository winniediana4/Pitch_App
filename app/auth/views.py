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
   user = user.query.filter_by(username).first()
   if user is None:
     error = 'None existant Username'
     return render_template('login.html',error = error)
   is_correct_password = user.check_password(password)
   print(is_correct_password)
   if not is_correct_password:
     error = 'None existant password'


     return render_template('login.html', error = error)
     login_user(user)
     return redirect('/')

     @auth.route('/signup', methods = ['GET', 'POST'])
     def signup():
       if request.method == 'POST':
         form = request.form
         username = form.get("password")
         confirm_password = form.get("confirm_password")
         if username is None or password is None or email is None or confirm_password is None:
           error = 'Username should be one word'
           return render_template('signup.html',error = error)
         else:
           user = User.query.filter_by(username = username).first()
           if user is not None:
             error = 'Email already exists'
             return render_template('signup.html', error = error)
           user = User(username=username, email = email )
           user.set_pasword(password)
           user.save()
       