# -*- coding: utf-8 -*-
from flask import Flask
from ScanServer.extensions import bootstrap

app = Flask('ApiServer')
app.config[ "SECRET_KEY"] =  "s_e_c_r_e_t_k_e_y_h_u_c_t_f"

def create_app(app):
    register_extensions(app)

def register_extensions(app):
    bootstrap.init_app(app)


create_app(app)

@app.errorhandler(400)
def bad_request(e):
    return render_template('404.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

from .views import *