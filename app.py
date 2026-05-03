from flask import Flask
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PASSWORD = os.getenv("DB_PASSWORD", "not set")

@app.route('/')
def home():
    return f"App is running V2! DB_HOST: {DB_HOST}"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
