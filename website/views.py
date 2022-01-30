#all the pages not related to authentication that user can nav to are here
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"

    
