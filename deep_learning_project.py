# -*- coding: utf-8 -*-
"""Deep Learning Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ECR1r0ju2UjBAVsLp2OsUimyAxeQ1lR5
"""

from google.colab import drive
drive.mount('/content/drive')

import os
import cv2
import numpy
import imageio
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution3D, MaxPooling3D
from keras.optimizers import SGD, RMSprop
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils, generic_utils
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
from keras import backend as K
import sys
K.set_image_dim_ordering('th')

image_rows, image_columns, image_depth = 64, 64, 18

training_list = []
painpath = '/content/drive/My Drive/Training Data/pain'
Nopainpath = '/content/drive/My Drive/Training Data/Nopain'

directorylisting = os.listdir(painpath)

for video in os.listdir(painpath):
  videopath = os.path.join(painpath, video)
  frames = []
  for image_path in os.listdir(videopath):
        input_path = os.path.join(videopath, image_path)
        image = cv2.imread(input_path)
        imageresize = cv2.resize(image, (image_rows, image_columns), interpolation = cv2.INTER_AREA)
        grayimage = cv2.cvtColor(imageresize, cv2.COLOR_BGR2GRAY)
        frames.append(grayimage)
  frames = numpy.asarray(frames)
  videoarray = numpy.rollaxis(numpy.rollaxis(frames, 2, 0), 2, 0)
  training_list.append(videoarray)

len(training_list)

directorylisting = os.listdir(Nopainpath)

for video in os.listdir(Nopainpath):
  videopath = os.path.join(Nopainpath, video)
  frames = []
  for image_path in os.listdir(videopath):
        input_path = os.path.join(videopath, image_path)
        image = cv2.imread(input_path)
        imageresize = cv2.resize(image, (image_rows, image_columns), interpolation = cv2.INTER_AREA)
        grayimage = cv2.cvtColor(imageresize, cv2.COLOR_BGR2GRAY)
        frames.append(grayimage)
  frames = numpy.asarray(frames)
  videoarray = numpy.rollaxis(numpy.rollaxis(frames, 2, 0), 2, 0)
  training_list.append(videoarray)

len(training_list)

training_list = numpy.asarray(training_list)
trainingsamples = len(training_list)
traininglabels = numpy.zeros((trainingsamples, ), dtype = int)

traininglabels[0:6] = 0
traininglabels[6:12] = 1

traininglabels = np_utils.to_categorical(traininglabels, 2)

training_data = [training_list, traininglabels]
(trainingframes, traininglabels) = (training_data[0], training_data[1])
training_set = numpy.zeros((trainingsamples, 1, image_rows, image_columns, image_depth))

training_set.shape

for h in range(trainingsamples):
    training_set[h][0][:][:][:] = trainingframes[h, :, :, :]

training_set = training_set.astype('float32')
training_set -= numpy.mean(training_set)
training_set /= numpy.max(training_set)

model = Sequential()
model.add(Convolution3D(4, (3, 3, 15), input_shape=(1, image_rows, image_columns, image_depth), activation='relu'))
model.add(MaxPooling3D(pool_size=(3, 3, 3)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(2, init='normal'))
model.add(Activation('softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer = 'SGD', metrics = ['accuracy'])
model.summary()

testing_list = []
painpath = '/content/drive/My Drive/TestingData/pain'
Nopainpath = '/content/drive/My Drive/TestingData/Nopain'

for video in os.listdir(painpath):
  videopath = os.path.join(painpath, video)
  frames = []
  for image_path in os.listdir(videopath):
        input_path = os.path.join(videopath, image_path)
        image = cv2.imread(input_path)
        imageresize = cv2.resize(image, (image_rows, image_columns), interpolation = cv2.INTER_AREA)
        grayimage = cv2.cvtColor(imageresize, cv2.COLOR_BGR2GRAY)
        frames.append(grayimage)
  frames = numpy.asarray(frames)
  videoarray = numpy.rollaxis(numpy.rollaxis(frames, 2, 0), 2, 0)
  testing_list.append(videoarray)

for video in os.listdir(Nopainpath):
  videopath = os.path.join(Nopainpath, video)
  frames = []
  for image_path in os.listdir(videopath):
        input_path = os.path.join(videopath, image_path)
        image = cv2.imread(input_path)
        imageresize = cv2.resize(image, (image_rows, image_columns), interpolation = cv2.INTER_AREA)
        grayimage = cv2.cvtColor(imageresize, cv2.COLOR_BGR2GRAY)
        frames.append(grayimage)
  frames = numpy.asarray(frames)
  videoarray = numpy.rollaxis(numpy.rollaxis(frames, 2, 0), 2, 0)
  testing_list.append(videoarray)

len(testing_list)

testing_list = numpy.asarray(testing_list)
testingsamples = len(testing_list)
testinglabels = numpy.zeros((testingsamples, ), dtype = int)

testinglabels[0:5] = 0
testinglabels[5:10] = 1

testinglabels = np_utils.to_categorical(testinglabels, 2)

testing_data = [testing_list, testinglabels]
(testingframes, testinglabels) = (testing_data[0], testing_data[1])
testing_set = numpy.zeros((testingsamples, 1, image_rows, image_columns, image_depth))

testing_set.shape

for h in range(testingsamples):
    testing_set[h][0][:][:][:] = testingframes[h, :, :, :]

testing_set = testing_set.astype('float32')
testing_set -= numpy.mean(testing_set)
testing_set /= numpy.max(testing_set)

hist = model.fit(training_set, traininglabels, epochs = 15, validation_data = (testing_set, testinglabels), shuffle=True)

predictions = model.predict(testing_set)
predictions_labels = numpy.argmax(predictions, axis=1)

predictions_labels

testinglabels = numpy.argmax(testinglabels, axis=1)

testinglabels

cfm = confusion_matrix(testinglabels, predictions_labels)
print (cfm)