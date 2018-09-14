from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User

class PostForm(FlaskForm):
    post = StringField('Tweet...', validators=[DataRequired()])
    submit = SubmitField('Post')

class TitleForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])
    submit = SubmitField('Change')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    password1 = PasswordField('Re-Type Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

    def validate_email(self, email):
       user = User.query.filter_by(email=email.data).first()
       if user is not None:
           flash('Email already taken.')
