from flask import Flask
from db import Store

app = Flask(__name__)

db = Store()


@app.route('/get/<int:pk>/')
def get(pk: int):
    test = db.get_link(pk)
    print(test)
    return dict(test)


if __name__ == '__main__':
    app.run()
