from flask import render_template, flash, redirect, url_for
from app import app
from flask_login import current_user, login_user, logout_user
from app.models import User
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = "Mister H"
    title = "Welcome"
    posts =[
        {"author": {'user':'Åsa'},
        'body':'it really is a beautifull day' 
        },
        {
            'author':{'user':'Peter'},
            'body':'Great day for coding Python'
        }
    ]
    return render_template('index.html', user=user, title=title, posts=posts)

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

    