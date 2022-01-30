from xmlrpc.client import boolean
from flask import Blueprint, render_template
from sqlalchemy import true

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html", boolean = True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

@auth.route('/secret-page')
def secret_page():
    return "<p>You found the secret page</p>"

