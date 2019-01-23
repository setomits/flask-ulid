from flask import Flask
from flask_ulid import ULIDConverter

app = Flask(__name__)
app.url_map.converters['ulid'] = ULIDConverter


@app.route('/article/<ulid:article_id>')
def article(article_id):
    return '{} is valid ulid'.format(article_id)
