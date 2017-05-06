# -*- coding: utf-8 -*-
# adminPages.py
from flask import Blueprint, render_template
from flask_login import current_user


home = Blueprint('home', __name__)


# leanote展示页, 没有登录的, 或已登录明确要进该页的
@home.route('/')
def index():

    return render_template('home/index.html', userInfo=current_user, title='dysz')
