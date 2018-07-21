#!/usr/bin/env python3
# -*- coding:utf8 -*-
import datetime
import flask
import redis
from flask import Flask
import six

app=Flask(__name__)
app.secret_key='HackIT'

r=redis.StrictRedis()

def event_stream():
    pubsub=r.pubsub()
    pubsub.subscribe('chat')
    for message in pubsub.listen():
        if isinstance(message['data'],bytes):
            message['data']=message['data'].decode('utf8')
        print(message)
        yield 'data: {}\n\n'.format(message['data'])

@app.route("/login",methods=['GET','POST'])
def login():
    if flask.request.method=="POST":
        flask.session['user']=flask.request.form['user']
        return flask.redirect('/')
    return '<form action="" method="post"> user: <input name="user">'

@app.route('/post',methods=['POST'])
def post():
    message=flask.request.form['message']
    user =flask.session.get('user','anonymous')
    now = datetime.datetime.now().replace(microsecond=0).time()

    r.publish('chat','[{}] {}: {}'.format(now.isoformat(),user,message))
    return flask.Response(status=204)

@app.route('/stream')
def stream():
    # limit mime type
    return flask.Response(event_stream(),mimetype="text/event-stream")

@app.route('/')
def home():
    if 'user' not in flask.session:
        return flask.redirect('/login')
    return flask.render_template('home.html')

if __name__ =='__main__':
    app.debug=True
    app.run()