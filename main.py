from flask import Flask, request, jsonify
from flask_cors import CORS # 👈 ADD THIS
import os

app = Flask(__name__)
CORS(app) # 👈 AND THIS

@app.route('/')
def home():
    return 'Backend is running ✅'

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello {name}!"})
