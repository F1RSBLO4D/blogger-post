from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,TextAreaField
from wtforms.validators import DataRequired,Length,Email

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    post_text = TextAreaField('Post Text', validators=[DataRequired()])
    submit = SubmitField('Add Post')


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')