# imports
# https://www.youtube.com/playlist?list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf
from python_speech_features import mfcc
import scipy.io.wavfile as wav
import numpy as np
from tempfile import TemporaryFile
import os
import pickle
import random 
import operator
import math
# import numpy as np
def distance(song1, song2, k):
    distance_ = 0
    song1_feature_1 = song1[0]
    song1_feature_2 = song2[1]
    song2_feature_1 = song2[0]
    song2_feature_2 = song2[1]
    distance_ = np.trace(np.dot(np.linalg.inv(song2_feature_2), song1_feature_2))
    diff = song2_feature_1 - song1_feature_1
    distance_ += np.dot(np.dot((diff).T, np.linalg.inv(song2_feature_2)), diff)
    distance_ += np.log(np.linalg.det(song2_feature_2) - np.log(np.linalg.det(song1_feature_2)))
    distance_ -= k
    return distance_
