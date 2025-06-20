
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello {name}!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
