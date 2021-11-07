import numpy as np
import pandas as pd
import os
path = "/home/nupur/MyntraHackathon/Fashion Dataset/myntradataset/"
csv_path = os.path.join(path,"styles.csv")
img_path = os.path.join(path,"images")
df = pd.read_csv(csv_path, error_bad_lines=False, warn_bad_lines=False,dtype=str)

df = df[df['baseColour'].notna()]
df['id'] = df['id'].apply(lambda x: str(x)+'.jpg')
df = df[df['id'].isin(os.listdir(img_path))]
df = df.reset_index(drop=True)
df = df.groupby(['usage']).filter(lambda x: len(x) >= 30)
print('DF shape:', df.shape)

from sklearn.model_selection import train_test_split
train_df, test_df = train_test_split(df,test_size = 0.1, random_state=42)
train_df, validation_df = train_test_split(df,test_size = 0.2, random_state=57)

print(df.dtypes)

df.head()

batch_size = 16

from keras_preprocessing.image import ImageDataGenerator

train_image_generator = ImageDataGenerator(
    rescale= 1./255,
    shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
    #validation_split=0.2
)
validation_image_generator = ImageDataGenerator(
    rescale= 1./255,
    #validation_split=0.2
)

training_generator = train_image_generator.flow_from_dataframe(
   
    dataframe=train_df,
    directory=img_path,
    x_col="id",
    y_col="usage",
    target_size=(96,96),
    batch_size=batch_size
  
)

validation_generator = validation_image_generator.flow_from_dataframe(
    dataframe=validation_df,
    directory=img_path,
    x_col="id",
    y_col="usage",
    target_size=(96,96),
    batch_size=batch_size,
    
)
test_generator = validation_image_generator.flow_from_dataframe(
    dataframe=test_df,
    directory=img_path,
    x_col="id",
    y_col="usage",
    target_size=(96,96),
    batch_size=batch_size,

   
)

classes = len(training_generator.class_indices)

print(training_generator.class_indices)

import tensorflow as tf
from tensorflow import keras
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, BatchNormalization,Dropout
from keras.models import Sequential

model = Sequential()

model.add(Conv2D(32,(3,3), activation = 'relu', input_shape = (96,96,3)))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Conv2D(32,(3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(BatchNormalization())
model.add(Conv2D(32,(3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(BatchNormalization())
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(classes, activation='softmax'))

model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss=tf.keras.losses.categorical_crossentropy, metrics=['accuracy'])
model.summary()
batch_size = 64
total_train = train_df.shape[0]
total_validation = validation_df.shape[0]
vgg_classifier = model.fit(training_generator,
steps_per_epoch=(total_train//batch_size),
epochs = 15,
validation_data=validation_generator,
validation_steps=(total_validation//batch_size),
batch_size = batch_size,
verbose=1)

model.save('modelForUsage.h5')
result = model.evaluate(test_generator,batch_size=batch_size)
print("test_loss, test accuracy",result)
