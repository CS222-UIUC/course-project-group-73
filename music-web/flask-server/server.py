
from io import BytesIO
from flask import jsonify, request, Flask
app = Flask(__name__)
from flask_cors import CORS
CORS(app)
from tensorflow import keras
import librosa
import sys
import numpy as np
import math
import librosa.display

# setting path
sys.path.append('../../')
 
# importing
from genre_classifier import load_data, plot_history, prepare_dataset, build_model, predict, actual_predict
 
#  venv\Scripts\activate\\\
# virtualenv venv
# using
# geek_method()
# print(add(100, 1000000))

model = keras.models.load_model('../../model.h5')
print(model)

import sys
 
# setting path
sys.path.append('../../')
# importing
from genre_classifier import add
# from ..genre_classifier import *
import os

print("running...")
print(add(1,2))
@app.route('/upload_file', methods=['POST'])
def upload_file():
    """Handles the upload of a file."""
    d = {}
    try: 
        file = request.files['file_from_react'] # .wav file (user input)
        print(type(file))
        filename = file.filename
    
        # validate the type of the file is .mp3 or .wav file:
        i = filename.rfind('.') # index of the period in file name
        file_ext = filename[i+1:]
        print(file_ext)
        if file_ext != 'mp3' and file_ext != 'wav':
            raise Exception("File type not supported")

        print(f"Uploading file {filename}")
        file_bytes = file.read()
        file_content = BytesIO(file_bytes).readlines()
        uploaded_file_path = os.path.join('uploads', 'jazz.00001.wav')
        print(uploaded_file_path)
        # file.save(os.path.join('./uploads', filename))
        # print(os.path.join('.\uploads', filename))
        # print(file_content)
        # save_mfcc('./uploads/' + filename)
        # audio_file = 
        # f_name = librosa.ex('./uploads/jazz.00000.wav')
        # print("why")
        # print
        # file_path = os.path.join('./uploads\\file.wav', f)
                # print(file_path))
        signal, sr = librosa.load(uploaded_file_path, sr=22050)
        print("not here")
        # print(signal.shape)
        # mfccs = librosa.feature.mfcc(signal, sr = sr, n_fft=2048, n_mfcc=13, hop_length=512)
        # print(mfccs)
        # print(mfccs.shape)
        # get_mat(signal, sr)
        # matrix = np.array(get_mat(signal, sr))
        # print(matrix.shape)
        # print(np.array(get_mat(signal, sr)).shape)
        print(np.array(get_mat(signal, sr)).shape)
        print(actual_predict(model, np.array(get_mat(signal, sr))))
        # print(actualPredict(model, mfccs.T))
        
        # print(signal.shape)
        d['status'] = 1

        # model.predict()

    except Exception as e:
        print(f"Couldn't upload file {e}")
        print(str(e))
        d['status'] = 0

    return jsonify(d)

def get_mat(signal, sr):
    SAMPLE_RATE = 22050
    DURATION = 30
    SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION
    num_samples_per_segment = int(SAMPLES_PER_TRACK / 6)
    # expected_num_mfcc_vectors_per_segment = math.ceil(num_samples_per_segment / 512)
    # print(expected_num_mfcc_vectors_per_segment) # 216
    expected_num_mfcc_vectors_per_segment = 216

    comb = []
    for s in range(6) :
        start_sample = num_samples_per_segment * s
        finish_sample = start_sample + num_samples_per_segment

        mfcc = librosa.feature.mfcc(y = signal[start_sample:finish_sample], sr = sr, n_fft=2048, n_mfcc=13, hop_length=512)
        mfcc = mfcc.T
        if len(mfcc) == expected_num_mfcc_vectors_per_segment:
            comb.append(mfcc.tolist())
        
    # print(comb)
    return comb

# save for a passed song:
# def save_mfcc(file_name, n_mfcc=13, n_fft=2048, hop_length=512):
#     # sample_rate = 22050
#     # duration = 30
#     # samples_per_track = sample_rate * duration
#     # num_samples_per_segment = int(samples_per_track / num_segments)

#     file_path = os.path.join(dirpath, f)
#     mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
#     mfccs = mfccs.T
#     print(mfccs)
#     return 3

if __name__ == '__main__':
    # run in development mode
    app.run(debug=True)