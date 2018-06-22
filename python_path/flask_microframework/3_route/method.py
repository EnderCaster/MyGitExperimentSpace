#!/usr/bin/env python3
import flask
app=flask.Flask(__name__)

@app.route('/login',method=['GET','POST'])
def login():
    if flask.request.method=='POST':
        # do_login()
        pass
    else:
        # show_login_form()
        pass