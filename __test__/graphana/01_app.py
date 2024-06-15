from flask import Flask, jsonify, request

app = Flask(__name__)

# Пример данных метаданных
metadata = {
    "service_name": "Example Service",
    "version": "1.0.0",
    "description": "This is an example service for demonstrating metadata retrieval.",
    "author": "Artem"
}

@app.route('/metadata', methods=['GET'])
def get_metadata():
    return jsonify(metadata)

if __name__ == '__main__':
    app.run(debug=True)