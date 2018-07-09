import flask
from flask import abort
from flask import redirect
from flask import url_for
from flask import render_template
from flask import session
from flask import escape
from flask import request

app = flask.Flask(__name__)


@app.route("/")
def index():
    if 'username' in session:
        return 'logged in as {}'.format(escape(session['username']))
    return redirect(url_for('login'))

@app.route("/login")
def login():
    if request.method=="POST":
        session['username']=request.form['username']
        return redirect(url_for('index'))
    return "assume there is a form"
@app.route("/errorhandler")
def error_401():
    abort(401)
    this_is_never_executed()


def this_is_never_executed():
    pass


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
@app.route('/logout')
def logout():
    # remove if username exist
    session.pop('username',None)
    return redirect(url_for('index'))
