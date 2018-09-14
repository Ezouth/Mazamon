from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import PostForm, TitleForm, LoginForm, RegisterForm
import datetime
from app.models import Post, User
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')
@app.route('/index')
@app.route('/index/<title>', methods=['GET', 'POST'])
def index(title=''):
    return render_template('index.html', title=title, page='home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Credentials are incorrect!')
            return redirect(url_for('login'))
        if login_user(user, remember=form.remember_me.data):
            flash('You are now logged in.')
            return redirect(url_for('index', email=user.email))


    return render_template('login.html', form=form, page='login')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you have successfully registered!')
        return redirect(url_for('login'))


    return render_template('register.html', form=form, page='register')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
