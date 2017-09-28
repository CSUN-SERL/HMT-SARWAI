# Systems Engineering Research Laboratory

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

from detection import EmotionClassifier

img = np.random.rand(48, 48, 1)

eclass = EmotionClassifier()
eclass.build()
emotions = eclass.predict_emotion(img)
print(emotions)