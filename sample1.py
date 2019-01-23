from flask import Flask
from flask_ulid import FlaskULID

app = Flask(__name__)
FlaskULID(app)


@app.route('/article/<ulid:article_id>')
def article(article_id):
    return '{} is valid ulid'.format(article_id)
