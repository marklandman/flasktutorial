__author__ = 'markl_000'

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views
