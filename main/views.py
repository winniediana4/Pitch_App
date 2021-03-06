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


@main.route('/new_post', methods = ['GET', 'POST'])
@login_required
def new_post():
  form = PostForm()
  if form.validate_on_submit():
    title = form.title.data
    post = form.post.data
    category = form.category.data
    user_id = current_user._get_current_object().id
    post_obj = post(post = post, title = title, category = category, user_id = user_id)
    
    post_obj.save()
    return redirect(url_for('main.index'))
  return render_template('pitch.html', form = form)


  @main.route('/comment/<int:post_id>', methods = ['GET', 'POST'])
  @login_required
  def comment(post_id):
    form = CommentForm()
    post = post.query.get(post_id)
    user = User.query.all()
    comments = comment.query.filter_by(post_id = post_id).all()
    if form.validate_on_submit():
      comment = form.comment.data  
      post_id = post_id
      user_id = current_user._get_current_object().id
      new_comment =comment(comment = comment, post_id = post_id, user_id = user_id)


      new_comment.save()
      new_comments = [new_comment]
      print(new_comments)
      return redirect(url_for('.comment', post_id = post_id))
    return render_template('comment.html', form = form, post = post, comments = comments, user = user)


    @main.route('/user')
    @login_required
    def user():
      username = current_user.username
      user = User.query.filter_by(username = username).first()
      if user is None:
        return('not found')
        return render_template('profile.html', user = user)


        @main.route('/user/<name>/update_profile', methods = ['POST', 'GET'])
        @login_required
        def updateprofile(name):
          form = UpdateProfile()
          user = User.query.filter_by(username = name).first()
          if user is None:
            error = 'The user does not exist'
          if form.validate_on_submit():
            user.bio = form.bio.data
            user.save()
            return redirect(url_for('.profile', name = name))
          return render_template('profile/update_profile.html', form = form) 

        @main.route('/like/<int:id>', methods =['POST', 'GET'])
        @login_required
        def upvote(id):
          post = post.query.get(id)
          new_vote = upvote(post = post, upvote = 1)
          new_vote.save()
          return redirect(url_for('main.posts'))


        @main.route('/dislike/<int:id>', methods = ['GET', 'POST'])
        @login_required
        def downvote(id):
          post = post.query(id)
          vm = Downvote(post = post, Downvote=1)
          vm = save()
          return redirect(url_for('main.post'))        