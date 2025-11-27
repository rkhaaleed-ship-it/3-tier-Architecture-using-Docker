from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "3-Tier Application Backend - Rawan",
        "status": "running", 
        "version": "1.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "backend"})

@app.route('/api/data')
def get_data():
    return jsonify({
        "data": ["item1", "item2", "item3"],
        "count": 3
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
