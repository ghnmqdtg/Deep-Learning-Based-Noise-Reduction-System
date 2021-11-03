# Settings for preparing the dataset
# NOISE_CLASS = 'Household_Appliance'
# NOISE_CLASS = 'TVnRadio'
# NOISE_CLASS = 'Vechicles'
NOISE_CLASS = 'Verbal_Human'
PATH_DIR_NOISE_SOURCE = './NOISE'
PATH_DIR_TRAIN_ROOT = f'./Train/{NOISE_CLASS}'

PATH_DIR_NOISE_CLASS = f'{PATH_DIR_NOISE_SOURCE}/{NOISE_CLASS}/'
PATH_DIR_VOICE_SOURCE = './TIMIT_CONVERTED_NORMALIZED/TRAIN/'
PATH_DIR_TRAIN_TIME_SERIES = f'{PATH_DIR_TRAIN_ROOT}/Time_serie/'
PATH_DIR_TRAIN_NOISE_dB = f'{PATH_DIR_TRAIN_ROOT}/scaled_dB/noise/'
PATH_DIR_TRAIN_VOICE_dB = f'{PATH_DIR_TRAIN_ROOT}/scaled_dB/voice/'
PATH_DIR_TRAIN_SPLIT_NOISY = f'{PATH_DIR_TRAIN_ROOT}/splitted/noisy/'
PATH_DIR_TRAIN_SPLIT_VOICE = f'{PATH_DIR_TRAIN_ROOT}/splitted/voice/'
PATH_DIR_TRAIN_SNR_BASED = f'{PATH_DIR_TRAIN_ROOT}/Noise_SNR/'
PATH_DIR_TRAIN_BLENDED_SOUND = f'{PATH_DIR_TRAIN_ROOT}/sound/'
PATH_DIR_TRAIN_IMAGE_NOISY = f'{PATH_DIR_TRAIN_ROOT}/image_noisy/'
PATH_DIR_TRAIN_IMAGE_VOICE = f'{PATH_DIR_TRAIN_ROOT}/image_voice/'
PATH_DIR_TRAIN_DATASET = f'{PATH_DIR_TRAIN_ROOT}/spectrogram'

# Parameters for preprocessing
SAMPLE_RATE = 16000
MIN_DURATION = 1.0
FRAME_SIZE = 18000
HOP_LENGTH_FRAME = 250
NB_SAMPLES = 8000
# N_FFT = 511
# HOP_LENGTH_FFT = 313
N_FFT = 256
HOP_LENGTH_FFT = 128
SLICE_LENGTH = 16384

# Settings for training
PATH_SPECROGRAM_HDF5_FILE = f'./Train/{NOISE_CLASS}/spectrogram/amp_db.h5'
MODEL = "FC"
# MODEL = "GRU"
MODEL_NAME = f'DDAE_{MODEL}_{NOISE_CLASS}'
PATH_WEIGHTS = f'./Train/{NOISE_CLASS}/weights/{MODEL_NAME}.h5'
TRAINING_FROM_SCRATCH = True
OPTIMIZER = "Adam"
SAVE_PERIOD = 25
# BATCH_SIZE = 53
BATCH_SIZE = 200
EPOCH_NUM = 500

# Settings for inference
PATH_DIR_TEST_ROOT = f'./demo_data/{NOISE_CLASS}/test/'
PATH_DIR_TEST_NOISE_dB = PATH_DIR_TEST_ROOT + 'scaled_dB/noise/'
PATH_DIR_TEST_VOICE_dB = PATH_DIR_TEST_ROOT + 'scaled_dB/voice/'
PATH_DIR_TEST_NOISE_PREDICT = PATH_DIR_TEST_ROOT + 'NOISE/'
PATH_DIR_TEST_VOICE_PREDICT = PATH_DIR_TEST_ROOT + 'TIMIT/'

PATH_DIR_PREDICT_ROOT = f'./demo_data/{NOISE_CLASS}/save_predictions/'
PATH_DIR_PREDICT_SNR_BASED = PATH_DIR_PREDICT_ROOT + 'Noise_SNR/'
PATH_DIR_SAVE_SPLIT_NOISY = PATH_DIR_PREDICT_ROOT + 'splitted/noisy/'
PATH_DIR_SAVE_SPLIT_VOICE = PATH_DIR_PREDICT_ROOT + 'splitted/voice/'
PATH_DIR_SAVE_NOISY = PATH_DIR_PREDICT_ROOT + 'NOISY/'
PATH_DIR_SAVE_IMAGE_NOISY = PATH_DIR_PREDICT_ROOT + 'image_noisy/'
PATH_DIR_SAVE_IMAGE_VOICE = PATH_DIR_PREDICT_ROOT + 'image_voice/'
PATH_DIR_SAVE_IMAGE_DENOISE = PATH_DIR_PREDICT_ROOT + 'image_denoise/'
PATH_PREDICT_OUTPUT_NAME = 'denoise_t2.wav'
