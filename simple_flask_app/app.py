import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/orders/computers', methods=['GET','POST'])
def order():
    # res = {
    #     "created_by": "1",
    #     "status": "QUEUED",
    #     "created_at": "time",
    #     "equipment": [
    #         "mouse", "keyboard"
    #     ]
    # }
    if request.method == 'GET':
        return jsonify(retrieve_orders())
    elif request.method == 'POST':
        return jsonify(create_orders(body=request.json))
    else:
        raise Exception('Unsupported HTTP request type.')

def retrieve_orders():
    return {}
def create_orders(data):
    return data

if __name__ == "__main__":
    app.run()