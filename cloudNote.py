# -*- coding: utf-8 -*-


from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from home.views import home
from auth.views import auth
from extensions import db,login_manager
from home.models import User

# create our little application :)





# Load default config and override config from an environment variable
# app.config.from_pyfile('conf/app.conf.py')
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)



def create_app():
    """Creates the app.

    :param config: The configuration file or object.
                   The environment variable is weightet as the heaviest.
                   For example, if the config is specified via an file
                   and a ENVVAR, it will load the config via the file and
                   later overwrite it from the ENVVAR.
    """
    app = Flask("cloudNote")

    #configure_app(app, config)
    #configure_celery_app(app, celery)
    configure_blueprints(app)
    configure_extensions(app)
    #configure_template_filters(app)
    #configure_context_processors(app)
    #configure_before_handlers(app)
    #configure_errorhandlers(app)
    #configure_logging(app)

    return app

def configure_app(app, config):
        """Configures FlaskBB."""
    # Use the default config and override it afterwards
    # app.config.from_object('flaskbb.configs.default.DefaultConfig')

   #

def configure_blueprints(app):
    app.register_blueprint(home,url_prefix='')
    app.register_blueprint(auth,url_prefix='')




def configure_extensions(app):
    """Configures the extensions."""

    # Flask-SQLAlchemy
    db.init_app(app)
    

    @login_manager.user_loader
    def load_user(user_id):
        """Loads the user. Required by the `login` extension."""

        user_instance = User.query.filter_by(id=user_id).first()
        if user_instance:
            return user_instance
        else:
            return None

    login_manager.init_app(app)


app =create_app()

app.run()
