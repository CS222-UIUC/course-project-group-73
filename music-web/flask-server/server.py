# from flask import Flask
# app = Flask(__name__)
# # example route
# @app.route('/api/members')
# def members():
#     return {'members': ['Jacob', 'Max', 'Daniel', 'David']}
# if __name__ == '__main__':
#     # run in development mode
#     app.run(debug=True)
from io import BytesIO
from flask import jsonify, request, Flask
app = Flask(__name__)
from flask_cors import CORS
CORS(app)

@app.route('/upload_file', methods=['POST'])
def upload_file():
    """Handles the upload of a file."""
    d = {}
    try:
        file = request.files['file_from_react']
        filename = file.filename
        print(f"Uploading file {filename}")
        file_bytes = file.read()
        file_content = BytesIO(file_bytes).readlines()
        print(file_content)
        d['status'] = 1

    except Exception as e:
        print(f"Couldn't upload file {e}")
        d['status'] = 0

    return jsonify(d)

if __name__ == '__main__':
    # run in development mode
    app.run(debug=True)