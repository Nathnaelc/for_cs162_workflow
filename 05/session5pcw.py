from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/basic-auth/<username>/<password>', methods=['GET'])
def basic_auth(username, password):
    # Extract the Authorization header
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({"error": "Missing Authorization header"}), 401

    # Split the header into 'Basic' and the encoded 'username:password'
    auth_type, auth_string = auth_header.split(' ')

    # Decode the base64 encoded string
    import base64
    decoded_auth_string = base64.b64decode(auth_string).decode('utf-8')

    # Split the string into username and password
    provided_username, provided_password = decoded_auth_string.split(':')

    # Check if the provided credentials match the expected credentials
    if provided_username == username and provided_password == password:
        return jsonify({"authenticated": True, "user": username})
    else:
        return jsonify({"authenticated": False}), 401


if __name__ == '__main__':
    app.run(debug=True)
