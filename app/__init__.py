import os
from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

app.config['APP_VERSION'] = os.environ.get('APP_VERSION', 'local')

from app import routes

