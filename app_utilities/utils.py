import matplotlib.pylab as plt
from matplotlib.backends.backend_agg import RendererAgg

import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
from io import BytesIO
import base64

import streamlit as st
from streamlit import caching

def crop_center(image):
  """Returns a cropped square image."""
  shape = image.shape
  new_shape = min(shape[1], shape[2])
  offset_y = max(shape[1] - shape[2], 0) // 2
  offset_x = max(shape[2] - shape[1], 0) // 2
  image = tf.image.crop_to_bounding_box(
      image, offset_y, offset_x, new_shape, new_shape)
  return image


def load_image(image, image_size=(500, 500), preserve_aspect_ratio=True):
  """Loads and preprocesses images."""
  # Load and convert to float32 numpy array, add batch dimension, and normalize to range [0, 1].
  img = plt.imread(image).astype(np.float32)[np.newaxis, ...]
  if img.max() > 1.0:
    img = img / 255.
  if len(img.shape) == 3:
    img = tf.stack([img, img, img], axis=-1)
  img = crop_center(img)
  img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
  return img

def show_images(images, titles):
  column = st.beta_columns(3)
  _lock = RendererAgg.lock
  with _lock:
    n = len(images)
    for i in range(n):
      column[i].image(images[i][0].numpy(), caption = titles[i], width = 500)

def download(images):
  image= images[2][0].numpy()
  image = Image.fromarray((image * 255).astype(np.uint8))
  buffered = BytesIO()
  image.save(buffered, format="jpeg")
  img_str = base64.b64encode(buffered.getvalue()).decode()
  href = f'<a href="data:file/jpg;base64,{img_str}" download="{"stylized.jpg"}"><input type="button" value="Download"></a>'
  return href


@st.cache(ttl = 900, max_entries = 3)
def load_model():
  model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
  return model

def transfer(model, content_image, style_image):

  outputs = model(tf.constant(content_image), tf.constant(style_image))
  stylized_image = outputs[0]
  return stylized_image


 