# -*- coding: utf-8 -*-
"""
    cloudNote.extensions
    ~~~~~~~~~~~~~~~~~~

    The extensions that are used by cloudNote.

    
"""
from celery import Celery
from flask_allows import Allows
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

from exceptions import AuthorizationRequired


# Permissions Manager
allows = Allows(throws=AuthorizationRequired)

# Database
db = SQLAlchemy()


# Celery
celery = Celery("cloudNote")
