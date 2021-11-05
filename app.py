from flask import Flask, request, redirect
from flask import jsonify
import models
from db import Store

app = Flask(__name__)

db = Store()
HOST_URL = 'http://127.0.0.1:5000/'


@app.route('/set/', methods=['POST'])
def set_link():
    request_data = request.get_json()

    if request_data and request_data.get('original_link'):
        original_link = request_data['original_link']
        link = db.create_link(models.Link(original=original_link))
        return HOST_URL + link.short
    else:
        return jsonify({'original_link': 'Обязательное поле'}), 400


@app.route('/<short>/', methods=['GET'])
def get_link(short: str):
    link = db.get_link_by_short(short)
    if link:
        return redirect(link.original)
    else:
        return 'Ссылка не найдена', 404


if __name__ == '__main__':
    app.run()
