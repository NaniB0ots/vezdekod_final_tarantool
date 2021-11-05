import uuid

from flask import Flask

import models
from db import Store

app = Flask(__name__)

db = Store()


@app.route('/get/<int:pk>/')
def get(pk: int):
    test = db.get_link(pk)
    print(test)
    return dict(test)


@app.route('/create/')
def create():
    db.create_link(models.Link(original='test1.com', short='short1.com'))
    return 'ok'


if __name__ == '__main__':
    app.run()
