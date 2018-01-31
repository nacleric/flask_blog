from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm, BlogForm
from app.models import User, Post
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
#@login_required
def index():
    if current_user.is_authenticated:
        user=current_user.username
    else:
        user='Stranger'
    posts=Post.query.all()
    #form=BlogForm()
    #if form.validate_on_submit():
    #    post=Post(body=form.body.data, author=current_user)
    return render_template('index.html', title='Home',user=user,posts=posts)
    #return render_template('index.html', title='Home', user=current_user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/admin', methods=['GET','POST'])
def admin():
    if current_user.is_anonymous:
        return redirect(url_for('index'))
    form = BlogForm()
    if form.validate_on_submit():
        post = Post(body=form.text.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
        #return 'form has been submitted'
    return render_template('adminui.html',form=form)
