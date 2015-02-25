#!\flaskarea\scripts\python
__author__ = 'markl_000'

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import data_required

class LoginForm(Form):
    openid = StringField('openid',validators=[data_required()])
    remember_me = BooleanField('remember_me',default=False)
