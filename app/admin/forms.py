
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    title = StringField('Blog Title', validators=[Required()])

    description = StringField('Description', validators=[Required()])

    blog = TextAreaField('Blog')

    submit = SubmitField('Submit')
