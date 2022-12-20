from flask import Flask
 
app = Flask(__name__, static_folder='static')
 
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '9a94c458105c28bce7c7198d236760a39e1e1e97d48045e7'
 
from app import views  # noqa