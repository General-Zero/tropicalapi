import json
from flask import Flask, jsonify, request
app = Flask(__name__)
content = 'To create an api using Flask, you need to first install it using pip install flask, then use the code:\nfrom flask import Flask and read the documents https://pypi.org/projects/Flask'
storage = [{'title': 'Create an api', 'content': f'{content}'}]
@app.route('/storage', methods=['GET'])
def get_storage():
    return jsonify(storage)

@app.route('/post', methods=['POST'])
def post_storage():
    if request.is_json:
        new_data = request.get_json()
        storage.append(new_data)
        return jsonify(new_data), 201
    return jsonify({'An error occured, please fix some errors or try again.'}), 400
if __name__ == '__main__':
    app.run(port=5000)
