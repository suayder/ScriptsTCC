from keras.applications.xception import Xception
from keras.models import Sequential, Model
from keras.layers import Dense, GlobalAveragePooling2D,Dropout
from keras.utils import plot_model
import numpy as np

np.random.seed(7)

base_model = Xception(include_top=True, weights='imagenet', input_tensor=None, input_shape=(299,299,3))
xception_model = Model(inputs=base_model.input, outputs = base_model.get_layer('avg_pool').output)
#plot_model(xception_model, to_file='model.png')
print(xception_model.summary())

""" singleLayer_model = Sequential()
singleLayer_model.add(Dense(256, input_dim = 25088, activation='relu'))
singleLayer_model.add(Dropout(0.5, noise_shape=None, seed=None))
singleLayer_model.add(Dense(2, activation='softmax'))
singleLayer_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
 """
#plot_model(singleLayer_model, to_file='../gopalakrishnan/model.png')
#print(singleLayer_model.summary())
#print(singleLayer_model.outputs)
#print(singleLayer_model.get_config())