__author__ = 'markl_000'

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Mark'}
    posts = [
        {
            'author': {'nickname':'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author':{'nickname':'Susan'},
            'body': 'The Avenger movie was so cool!'
        },
        {
            'author':{'nickname':'Charlie'},
            'body': 'I gotta return my stuff dude'
        }

    ]
    return render_template('index.html',
                           title = 'home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',title='Sign In',form=form)
