from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Apply CORS to this app
CORS(app)

@app.route('/')
def front_page():
    return 'Welcome to the Flask API!'


if __name__ == '__main__':
    # TODO: Have DEBUG=False in production
    app.run(debug=True)