# -*- coding: utf-8 -*-
# adminPages.py
from flask import Blueprint,render_template


home = Blueprint('home', __name__)


@home.route('/')
def admin_login():
    return render_template('home/index.html')



