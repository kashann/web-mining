import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

input_shape = (28, 28, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

x_train /= 255
x_test /= 255

print(x_train.shape)

model = Sequential()
model.add(Conv2D(28, kernel_size=(3, 3), input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation=tf.nn.relu)) #max(0,x)
model.add(Dropout(0, 2))
model.add(Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x=x_train, y=y_train, epochs=10)
model.evaluate(x_test, y_test)

test_index = 1111
print(y_test[test_index])
prediction = model.predict(x_test[test_index].reshape(1, 28, 28, 1))
print(prediction.argmax())