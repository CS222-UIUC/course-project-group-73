
from io import BytesIO
from flask import jsonify, request, Flask
app = Flask(__name__)
from flask_cors import CORS
CORS(app)
from tensorflow import keras
import sys
 
# setting path
sys.path.append('../../')
 
# importing
from genre_classifier import load_data, plot_history, prepare_dataset, build_model, predict
 
#  venv\Scripts\activate\\\
# virtualenv venv
# using
# geek_method()
# print(add(100, 1000000))

model = keras.models.load_model('../../model.h5')
print(model)

@app.route('/upload_file', methods=['POST'])
def upload_file():
    """Handles the upload of a file."""
    d = {}
    try:
        file = request.files['file_from_react']
        print(type(file))
        filename = file.filename
        print(f"Uploading file {filename}")
        file_bytes = file.read()
        file_content = BytesIO(file_bytes).readlines()
        print(file_content)
        d['status'] = 1

        # model.predict()

    except Exception as e:
        print(f"Couldn't upload file {e}")
        d['status'] = 0

    return jsonify(d)

if __name__ == '__main__':
    # run in development mode
    app.run(debug=True)