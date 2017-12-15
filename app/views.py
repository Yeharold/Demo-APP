#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-13 08:45:49
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : http://example.org

from app import *
from flask import request, render_template, session, redirect, url_for
from app.models import *


@app.route('/sigin', methods=['POST', 'GET'])
def sigin():

    if request.method == 'POST':
        username = request.form['user']
        pwd1 = request.form['pwd1']
        pwd2 = request.form['pwd2']

        if pwd1 == pwd2:

            sigIn(username, pwd1)
            return redirect('/login')
        else:

            return 'two password is different'

    return render_template('sigin.html')


@app.route('/login', methods=['POST', 'GET'])
def log():

    if request.method == "POST":
        username = request.form['user']
        password = request.form['pwd1']

        userInfo = loginCheck(username)

        if len(userInfo) != 0:

            if userInfo[0][1] == password:
                session['username'] = username
                return render_template('index.html')

            else:
                return render_template('pwd_error.html')

        else:
            return render_template('unsigin_error.html')

    return render_template('login.html')


@app.route('/index')
def index():

    username = session['user']
    if username != "":

        return render_template('index.html')

    return 'you have not sigin'


@app.route('/logout', methods=['POST', 'GET'])
def logout():

    if request.method == 'POST':
        session.pop('user', None)

        return redirect('/login')
