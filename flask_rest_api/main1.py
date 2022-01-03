from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'beautiful store',
        'items': [
            {
                'name': 'flowers',
                'price': 100
            }
        ]
    },
    {
        'name': 'beautiful store1',
        'items': [
            {
                'name': 'books',
                'price': 200
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    new_store = {
        'name': data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    for store in stores:
        if store['name'] == name:
            data = request.get_json()
            new_item = {
                'name': data['name'],
                'price': data['price']
            }
            store['name'].append(new_item)
            return jsonify(new_item)
        return jsonify({'message': 'not found'})


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['name'])
        return jsonify({'message': 'no store found'})


@app.route('/store/<string:name>/item')
def get_store_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
        return jsonify({'message': 'no store found'})


if __name__ == '__main__':
    app.run(debug=True)
