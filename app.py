from flask import Flask, jsonify, request

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

# POST /store {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store():
    # itterate over stores
    # if store name matches, return it
    # If none match, return an error message

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item/', methods=['POST'])
def create_item_in_store():
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store():
    pass

app.run(port=5002)
