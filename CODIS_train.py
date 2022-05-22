from keras.models import Sequential
from keras.layers import Dense, LSTM, Bidirectional
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from scipy.ndimage import gaussian_filter1d
from scipy.signal import medfilt

#預測輸入的時間戳記數(天)
n_timestamp = 10

np.random.seed(11)

train_set = pd.read_csv('train.csv')
test_set = pd.read_csv('test.csv')
#值過濾和高斯過濾
train_set['Temperature'] = medfilt(train_set['Temperature'], 3)
train_set['Temperature'] = gaussian_filter1d(train_set['Temperature'], 1.2)
test_set['Temperature'] = medfilt(test_set['Temperature'], 3)
test_set['Temperature'] = gaussian_filter1d(test_set['Temperature'], 1.2)

training_set = train_set.iloc[:,1:2].values
testing_set = test_set.iloc[:,1:2].values

#資料標準化0到1
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)
testing_set_scaled = sc.fit_transform(testing_set)

def data_split(sequence, n_timestamp):
    X = []
    y = []
    for i in range(len(sequence)):
        end_ix = i + n_timestamp
        if end_ix > len(sequence)-1:
            break
        # i to end_ix as input
        # end_ix as target output
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)

X_train, y_train = data_split(training_set_scaled, n_timestamp)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test, y_test = data_split(testing_set_scaled, n_timestamp)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)