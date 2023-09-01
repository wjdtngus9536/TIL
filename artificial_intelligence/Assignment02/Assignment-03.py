# -*- coding: utf-8 -*-
"""06_04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dxnYUJVXUnKcn0qCAsZxlAvDlWt4IODI
"""

# Assignment-03.py

import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout
from tensorflow.keras.optimizers import Adam

# n순위 정확도 구하는 함수
def top_N_Accuracy(convolutional_neural_network, x_test, y_test, n):
    # 실제 클래스(index) (10,000, 1) 텐서
    y_test_label = np.argmax(y_test, axis = 1)[:, None]

    # 해당 클래스가 주어진 입력에 대한 올바른 클래스일 확률들 출력 (10,000, 10) 텐서
    y_predict = convolutional_neural_network.predict(x_test)    
    # 순위 내림차순 정렬
    y_pred_order = np.argsort(y_predict, axis=1)[:, ::-1]
    
    # n순위 이내에 실제 클래스가 있는지 확인
    correct_predictions = np.mean(np.any(y_pred_order[:, :n] == y_test_label, axis=1))

    print(n,"순위 정확률은", correct_predictions * 100)

# CIFAR-10 데이터셋을 읽고 신경망에 입력할 형태로 변환
(x_train,y_train),(x_test,y_test)=cifar10.load_data()
x_train=x_train.astype(np.float32)/255.0
x_test=x_test.astype(np.float32)/255.0
y_train=tf.keras.utils.to_categorical(y_train,10)
y_test=tf.keras.utils.to_categorical(y_test,10)

# 신경망 모델 설계
cnn=Sequential()
cnn.add(Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)))
cnn.add(Conv2D(32,(3,3),activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2,2)))
cnn.add(Dropout(0.25))
cnn.add(Conv2D(64,(3,3),activation='relu'))
cnn.add(Conv2D(64,(3,3),activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2,2)))
cnn.add(Dropout(0.25))
cnn.add(Flatten())
cnn.add(Dense(512,activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(10,activation='softmax'))

# 신경망 모델 학습
cnn.compile(loss='categorical_crossentropy',optimizer=Adam(),metrics=['accuracy'])
hist=cnn.fit(x_train,y_train,batch_size=128,epochs=30,validation_data=(x_test,y_test),verbose=2)

# 신경망 모델 정확률 평가
res=cnn.evaluate(x_test,y_test,verbose=0)
print("정확률은",res[1]*100)

# 5순위 정활률
top_N_Accuracy(cnn, x_test, y_test, 5)


import matplotlib.pyplot as plt

# 정확률 그래프
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train','Validation'], loc='best')
plt.grid()
plt.show()

# 손실 함수 그래프
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train','Validation'],loc='best')
plt.grid()
plt.show()
cnn.save("/content/drive/MyDrive/savedModels/cnn06_04.h5")

# n순위 정확도 구하는 함수
def top_N_Accuracy(convolutional_neural_network, x_test, y_test, n):
    # 실제 클래스(index) (10,000, 1) 텐서
    y_test_label = np.argmax(y_test, axis = 1)[:, None]

    # 해당 클래스가 주어진 입력에 대한 올바른 클래스일 확률들 출력 (10,000, 10) 텐서
    y_predict = convolutional_neural_network.predict(x_test)    
    # 순위 내림차순 정렬
    y_pred_order = np.argsort(y_predict, axis=1)[:, ::-1]
    
    # n순위 이내에 실제 클래스가 있는지 확인
    correct_predictions = np.mean(np.any(y_pred_order[:, :n] == y_test_label, axis=1))

    print(n,"순위 정확률은", correct_predictions * 100)

for i in range(6):
    top_N_Accuracy(cnn, x_test, y_test, i)

np.any(y_pred_order[:, :5] == np.argmax(y_test, axis=1)[:, None], axis=1)

print(y_pred_order[:10, :5])

temp = np.argmax(y_test, axis = 1)[:, None]
temp[:10, :5]