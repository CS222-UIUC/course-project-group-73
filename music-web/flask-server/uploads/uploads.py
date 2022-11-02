import sys
 
# setting path
sys.path.append('../../../')

from genre_classifier import load_data, plot_history, prepare_dataset, build_model, predict, actualPredict

from data import save_mfcc, SAMPLE_RATE, SAMPLES_PER_TRACK, DURATION

