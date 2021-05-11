import logging

from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

# We need not call run() because our app is embedded within the App Engine WSGI application server.

@app.route('/')
def hello():
    return 'Hello!'

@app.errorhandler(404)
def page_not_found(e):
    logging.exception('A request was made for a non-existant resource.')
    return 'Nothing found at this URL.'

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
