# Assignment-02.py
'''
02. 6-2.py는 활성 함수로 ReLU를 사용한다. 
19, 20, 24행에서 relu를 sigmoid로 변경해 성능을 비교하고, 각각의 정확률, 정확률 그래프, 손실 함수 그래프를 첨부하시오.
'''
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout
from tensorflow.keras.optimizers import Adam

# MNIST 데이터셋을 읽고 신경망에 입력할 형태로 변환
(x_train,y_train),(x_test,y_test)=mnist.load_data()
x_train=x_train.reshape(60000,28,28,1)
x_test=x_test.reshape(10000,28,28,1)
x_train=x_train.astype(np.float32)/255.0
x_test=x_test.astype(np.float32)/255.0
y_train=tf.keras.utils.to_categorical(y_train,10)
y_test=tf.keras.utils.to_categorical(y_test,10)

# 신경망 모델 설계
cnn=Sequential()
cnn.add(Conv2D(32,(3,3),activation='sigmoid',input_shape=(28,28,1)))
cnn.add(Conv2D(64,(3,3),activation='sigmoid'))
cnn.add(MaxPooling2D(pool_size=(2,2)))
cnn.add(Dropout(0.25))
cnn.add(Flatten())
cnn.add(Dense(128,activation='sigmoid'))
cnn.add(Dropout(0.5))
cnn.add(Dense(10,activation='softmax'))

# 신경망 모델 학습
cnn.compile(loss='categorical_crossentropy',optimizer=Adam(),metrics=['accuracy'])
hist=cnn.fit(x_train,y_train,batch_size=128,epochs=12,validation_data=(x_test,y_test),verbose=2)

# 신경망 모델 정확률 평가
res=cnn.evaluate(x_test,y_test,verbose=0)
print("정확률은",res[1]*100)

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
plt.legend(['Train','Validation'], loc='best')
plt.grid()
plt.show()

'''
Epoch 1/12
469/469 - 7s - loss: 2.4147 - accuracy: 0.1017 - val_loss: 2.3031 - val_accuracy: 0.1028 - 7s/epoch - 15ms/step
Epoch 2/12
469/469 - 5s - loss: 2.3150 - accuracy: 0.1042 - val_loss: 2.3021 - val_accuracy: 0.1028 - 5s/epoch - 10ms/step
Epoch 3/12
469/469 - 4s - loss: 2.3053 - accuracy: 0.1046 - val_loss: 2.3015 - val_accuracy: 0.1135 - 4s/epoch - 9ms/step
Epoch 4/12
469/469 - 4s - loss: 2.3046 - accuracy: 0.1080 - val_loss: 2.3022 - val_accuracy: 0.1135 - 4s/epoch - 9ms/step
Epoch 5/12
469/469 - 4s - loss: 2.3047 - accuracy: 0.1045 - val_loss: 2.3020 - val_accuracy: 0.1135 - 4s/epoch - 8ms/step
Epoch 6/12
469/469 - 4s - loss: 2.3042 - accuracy: 0.1084 - val_loss: 2.3055 - val_accuracy: 0.1135 - 4s/epoch - 10ms/step
Epoch 7/12
469/469 - 4s - loss: 2.3039 - accuracy: 0.1083 - val_loss: 2.3027 - val_accuracy: 0.1032 - 4s/epoch - 8ms/step
Epoch 8/12
469/469 - 4s - loss: 2.3043 - accuracy: 0.1081 - val_loss: 2.3037 - val_accuracy: 0.0980 - 4s/epoch - 8ms/step
Epoch 9/12
469/469 - 4s - loss: 2.3044 - accuracy: 0.1058 - val_loss: 2.3037 - val_accuracy: 0.1009 - 4s/epoch - 9ms/step
Epoch 10/12
469/469 - 4s - loss: 2.3047 - accuracy: 0.1064 - val_loss: 2.3028 - val_accuracy: 0.1135 - 4s/epoch - 9ms/step
Epoch 11/12
469/469 - 4s - loss: 2.3040 - accuracy: 0.1060 - val_loss: 2.3021 - val_accuracy: 0.1135 - 4s/epoch - 9ms/step
Epoch 12/12
469/469 - 4s - loss: 2.3044 - accuracy: 0.1050 - val_loss: 2.3020 - val_accuracy: 0.1135 - 4s/epoch - 9ms/step
정확률은 11.349999904632568
'''