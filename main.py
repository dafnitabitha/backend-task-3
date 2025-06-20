from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Backend is running ✅'

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello {name}!"})
