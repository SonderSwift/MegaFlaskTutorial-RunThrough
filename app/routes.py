"""
render_template: renders the template html files using jinja2 by default
redirect: sends user to specified page
url_for: generates adaptive URLs using internal mapping of views
app: flask App instantiated in __init__
LoginForm: login class
"""

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from random import randrange

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jacky'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():  # POST request and field validation works
        # - create message, store in flask flash
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
    	# - access in template to show message to user

        # navigate to index page
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/random', methods=['GET', 'POST'])
def rn():
    return str(randrange(1000))




