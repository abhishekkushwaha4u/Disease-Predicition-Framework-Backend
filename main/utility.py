import numpy as np
import tensorflow as tf
from PIL import Image



def image_predicition(input_image, model):
    output_image = Image.open(input_image)
    output_image = output_image.resize((64,64))
    output_image = tf.keras.preprocessing.image.img_to_array(output_image)
    output_image = np.expand_dims(output_image, axis = 0)
    result = model.predict(output_image)
    return result[0][0]