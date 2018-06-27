import flask
from flask import request
app = flask.Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    err = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return login_user(request.form['username'])
        else:
            error = 'Invalid user/password'
        # the code under the line is a practice of cookie
        cookieResp = flask.make_response(flask.render_template('login.html'))
        cookieResp.set_cookie('username', 'username_hashed')
        return cookieResp
    if request.method == 'GET':
        cookie = request.cookie.get('username')
        if is_login(cookie):
            return login_user()
    return flask.render_template('login.html', error=error)

# we can also use request.args.get('username','guest') to get the params in get


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file_name']
        f.save('/tmp/web_saved_file')


def is_login(cookie):
    pass


def login_user(username=''):
    pass


def valid_login(username='', password=''):
    pass
