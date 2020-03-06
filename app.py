from flask import Flask

app = Flask(__name__)

# POST /store {name:}
@app.route('/store')

# GET /store/<string:name>
# GET /store
# POST /store/<string:name>/item {name:, price:}
# GET /store/<string:name>/item






app.run(port=5001)
