from flask import Flask, jsonify, request

app = Flask(__name__)

# Example GET endpoint
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

# Example POST endpoint
@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    print(f"data - {data}")
    return jsonify({"received": data}), 201

if __name__ == '__main__':
    app.run(debug=True)
