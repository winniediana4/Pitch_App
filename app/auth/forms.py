from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class PostForm(FlaskForm):
  title = StringField('Title', validators = [Required()])
  post = TextAreaField('pitch',validators = [Required()])
  category = SelectField('Category', choices = [('PRODUCT', 'PRODUCT'),('IDEA'), 'Business', 'Business'], validators = [Required()])

  submit = SubmitField('post')


  class CommentForm(FlaskForm):
    comment = TextAreaField('comment', validators = [Required()])
    submit = SelectField('post')


    class Vote(FlaskForm):
      submit = SelectField('like')

      class UpdateProfile(FlaskForm):
        bio = TextAreaField('bio', validators = [Required()])
        submit = SubmitField('post')
