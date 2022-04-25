import time
from flask_cors import CORS
from flask import Flask, jsonify, make_response

app = Flask(__name__)
CORS(app)

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}
