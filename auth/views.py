# -*- coding: utf-8 -*-
"""
    flaskbb.auth.views
    ~~~~~~~~~~~~~~~~~~

    This view provides user authentication, registration and a view for
    resetting the password of a user if he has lost his password

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
from datetime import datetime

from flask import Blueprint, flash, redirect, url_for, request, render_template,redirect,jsonify
from flask_login import current_user, login_user, login_required,logout_user, confirm_login, login_fresh
from flask_babelplus import gettext as _
from exceptions import AuthenticationError
from home.models import User


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET"])
def login( noteUrl=''):
    #Logs the user in.
    if current_user is not None and current_user.is_authenticated:
        return redirect(url_for("home.index"))   

    return render_template("home/login.html",
                           noteUrl=noteUrl)

@auth.route("/doLogin", methods=["POST"])
def doLogin():
    #Logs the user in.
    msg=''
    email= request.form['email']
    pwd= request.form['pwd']
    try:
        user = User.authenticate(email, pwd)
        if not login_user(user, remember=False):
            msg = ("In order to use your account you have to activate it "
                    "through the link we have sent to your email "
                    "address.")
        
        return redirect_or_next(url_for("home.index"))
    except AuthenticationError:
        flash("Wrong username or password.")

    return render_template("home/login.html", noteUrl='')
    


