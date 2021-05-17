import logging
import os

from flask import Flask
from google.cloud import storage

app = Flask(__name__)
app.config['DEBUG'] = True
CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']


# We need not call run() because our app is embedded within the App Engine WSGI application server.


@app.route('/')
def hello():
    return 'Hello!'

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files.get('file')

    if not uploaded_file:
        return 'No file uploaded.', 400

    gcs = storage.Client()

    bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)

    blob = bucket.blob(uploaded_file.filename)
    blob.upload_from_string(uploaded_file.read(), content_type=uploaded_file.content_type)


@app.errorhandler(404)
def page_not_found(e):
    logging.exception('A request was made for a non-existant resource.')
    return 'Nothing found at this URL.'

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500


# if __name__ == '__main__':
    # use this if running locally.
    # TODO: make this work
