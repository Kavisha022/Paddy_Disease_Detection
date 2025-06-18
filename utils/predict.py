import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load model once
model = load_model('model/paddy_model.h5')
class_names = ['Brown Spot', 'Leaf Smut', 'Bacterial Blight']

# class_names = ['බ්‍රවුන් ස්පොට්', 'ලිෆ් ස්මට්', 'බැක්ටීරියා බ්ලයිට්']

def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(300, 300))  # adjust size
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    return class_names[class_index]
