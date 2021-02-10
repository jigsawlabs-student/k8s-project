from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/api/apartments')
def apartments():
    return jsonify([{'id': 1, 'address': '164 W. 26th Street', 'zipcode': 10001, 'bedrooms': 4, 'bathrooms': 2}, 
        {'id': 2, 'address': '335 E. 22nd Street', 'zipcode': 10010,  'bedrooms': 'studio', 'bathrooms': 1}])
