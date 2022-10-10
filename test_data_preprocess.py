import librosa
from data import *

file_path = "invalid_file_path"

def test_invalid_file_path():
    entered_except = False
    try:
        signal, sr = librosa.load(file_path, sr=data.SAMPLE_RATE)
    except:
        entered_except = True

    assert entered_except == True

# run assert tests
test_invalid_file_path()

# all test cases passed
print("all test cases passed for test_data_preprocess.py")