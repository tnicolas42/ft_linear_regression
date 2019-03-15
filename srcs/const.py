"""
this file contains all const
"""

# this is the default config to learn
LEARNING_RATE = 0.1
THETA = [0.0, 0.0]
NB_ITER = 3500

DATA_FILENAME = "data/data.csv"
DATA_KM = "km"
DATA_PRICE = "price"

THETA_FILENAME = "data/theta.json"  # file to load the learned theta

STOP_THRESHOLD = 1e-8  # threshold to auto stop the train
INCREASE_THRESHOLD = 100  # if the cost increase with more than 100 from the begining -> stop fitting
