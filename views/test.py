# -*- coding: utf-8 -*-
from views import *
from flask import (Blueprint, current_app, request, g, url_for, make_response,
                   render_template, redirect, jsonify)
from models.model_test import TestUser, flush
view = Blueprint('test', __name__, url_prefix='/test')

@view.route('/haha')
def haha():
    u = request.args.get('u')
    if u:
        try:
            u = TestUser(name=u)
            flush(u)
        except:
            return _('u duplicated!')
    us = TestUser.query.all()
    return render_template('test/haha.html', us=us)


@view.route('/style')
def style():
    return render_template('test/style.html')
