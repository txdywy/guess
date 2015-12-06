# -*- coding: utf-8 -*-
from views import *
from flask import (Blueprint, current_app, request, g, url_for, make_response,
                   render_template, redirect, jsonify, flash, session)
from models.model_test import *
from werkzeug import check_password_hash, generate_password_hash
from wsgi import app
import json
import functools


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


def login_required(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        if 'user_id' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return func


def power_required(power=User.POWER_ADMIN):
    def deco(f):
        @functools.wraps(f)
        def func(*args, **kwargs):
            if g.user.power & power:
                return f(*args, **kwargs)
            else:
                return redirect(url_for('login'))
        return func
    return deco


def exr(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception, e:
            return str(e)
    return func


@app.route('/gray')
def gray():
    return render_template('test/gray.html')
