# -*- coding: utf-8 -*-


from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from home.views import home

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
    #configure_extensions(app)
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
    

app =create_app()



app.run()
