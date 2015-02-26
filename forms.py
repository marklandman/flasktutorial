#!\flaskarea\scripts\python
__author__ = 'markl_000'

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import data_required, Length

class LoginForm(Form):
    openid = StringField('openid',validators=[data_required()])
    remember_me = BooleanField('remember_me',default=False)

class EditForm(Form):
    nickname = StringField('nickname', validators=[data_required()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
