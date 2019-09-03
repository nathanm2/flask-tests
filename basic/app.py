#!/usr/bin/env python3

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
        {
            'name': 'My Wonderful Store',
            'items': [
                {
                    'name': 'My Item',
                    'price': 15.99
                    }
                ]
            }
        ]

@app.route('/')
def home():
    return render_template('index.html')

# POST /store {name}
@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    new_store = {
            'name': data['name'],
            'items': []
            }
    stores.append(new_store)
    return jsonify(new_store)

# GET  /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store)
    return jsonify({'message': 'No store found'})

# GET  /store
@app.route('/store')
def get_stores():
    return jsonify(stores)

# POST /store/<name>/item {name, price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    data = request.get_json()
    for store in stores:
        if name == store['name']:
            new_item = {
                    'name': data['name'],
                    'price': data['price']
                    }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'No store found'})

# GET /store/<name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store['items'])
    return jsonify({'message': 'No store found'})


app.run(port=5000)
