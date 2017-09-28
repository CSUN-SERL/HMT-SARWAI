# Systems Engineering Research Laboratory

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import cv2
import numpy as np

from keras.models import Sequential
from keras.layers import Conv2D, Dropout, Flatten, Dense


class EmotionClassifier:

    def __init__(self):
        pass

    def build(self, image_shape=(48, 48, 1), channels_first=True, verbose=0):
        """Builds Emotion Classifier.

        Args:
            image_shape: A `tuple` that defines the input image shape.
            channels_first: A flag to signify that rgb channels are first or not.
            verbose: The flag to define the level of verbosity during the build
            process.

        Returns:
            A `boolean` if the build was sucessful.
        """

        self.model = Sequential()
        self.model.add(Conv2D(32, 3, 3, border_mode='same', activation='relu',
                         input_shape=image_shape))

        self.model.add(Conv2D(32, 3, 3, border_mode='same', activation='relu'))
        self.model.add(Conv2D(32, 3, 3, border_mode='same', activation='relu'))

        self.model.add(Conv2D(64, 3, 3, border_mode='same', activation='relu'))
        self.model.add(Conv2D(64, 3, 3, border_mode='same', activation='relu'))
        self.model.add(Conv2D(64, 3, 3, border_mode='same', activation='relu'))

        self.model.add(Conv2D(128, 3, 3, border_mode='same', activation='relu'))
        self.model.add(Conv2D(128, 3, 3, border_mode='same', activation='relu'))
        self.model.add(Conv2D(128, 3, 3, border_mode='same', activation='relu'))

        self.model.add(Flatten())

        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dropout(0.20))
        self.model.add(Dense(7, activation='relu'))
        self.model.add(Dropout(0.20))

        # optimizer:
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        return True

    def train(self, X, y, nb_epochs=100):
        """Trains model.

        """
        pass

        self.model.fit(X, y, nb_epoch=nb_epochs)

    def load_model(self):
        """Loads the saved model parameters.

        """
        pass

    def predict_emotion(self, face_image):
        """Predicts the emotion of a face.

        Args:
            face_image (ndarray): An image to use to predict emotion.

        Returns:

            dict: A dictionary of one-hot-encoded emotions as values with their corresponding keys.
        """

        resized_img = cv2.resize(face_image, (48, 48), interpolation=cv2.INTER_AREA)

        resized_img = np.expand_dims(resized_img, -1)
        resized_img = np.expand_dims(resized_img, 0)

        list_of_list = self.model.predict(resized_img, batch_size=1, verbose=1)
        angry, disgust, fear, happy, sad, surprise, neutral = [prob for lst in list_of_list for prob in lst]

        return [angry, disgust, fear, happy, sad, surprise, neutral]