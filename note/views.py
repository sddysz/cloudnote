# -*- coding: utf-8 -*-

from datetime import datetime

from flask import Blueprint, flash, redirect, url_for, request, render_template,redirect,jsonify,json
from flask_login import current_user, login_user, login_required,logout_user, confirm_login, login_fresh
from flask_babelplus import gettext as _
from exceptions import AuthenticationError
from home.user import User


note = Blueprint("note", __name__)


@auth.route("/login", methods=["GET"])
def login( noteUrl=''):
    #Logs the user in.
   

