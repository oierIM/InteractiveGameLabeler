from flask import Flask, jsonify
from flask_cors import CORS
import json
from labeler import json_path, image_path

app = Flask(__name__)
CORS(app)

@app.route('/json')
def get_button_coordinates():
    # Your code to generate the JSON response
    with open(json_path, 'r') as f:
        data = json.load(f)

    response = jsonify(data)
    return response

if __name__ == '__main__':
    app.run(debug=True, port=8000)
