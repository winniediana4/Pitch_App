from threading import main_thread
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from . import PostForm, CommentForm, UpdateProfile, main
from  ..models import post, Comment, User, Upvote, Downvote

@main_thread.route('/')
def index():
  posts = post.query.all()
  product = post.query.filter_by(category = 'product').all()
  idea = post.query.filter_by(category = 'idea').all()
  business = post.query.filter_by(category = ('Business').all()
  return render_template('index.html', business = business, product = product, idea = idea, posts = posts)


@main.route('/posts')
@login_required
def posts():
  posts = post.query.all()
  likes = upvote.query.all()
  user = current_user
  return render_template('pitch_display.html', posts = posts, likes = likes, user = user)


  


