import os
import tensorflow as tf
import numpy as np
import streamlit as st
from keras.models import load_model

st.header('Logo Identification Model')
clubs = ['barcelona', 'bayren munchen', 'liverpool', 'man utd', 'milan', 'real madrid']

# Correct the model path if necessary
model = load_model('Image_Classify_Model.keras')

def classify_images(image_path):
    input_image = tf.keras.utils.load_img(image_path, target_size=(224, 224))  # Ensure this matches training size
    input_image_array = tf.keras.utils.img_to_array(input_image)
    input_image_exp_dim = tf.expand_dims(input_image_array, 0)  # Add batch dimension

    predictions = model.predict(input_image_exp_dim)
    result = tf.nn.softmax(predictions[0])
   
    outcome = 'The image belongs to ' + clubs[np.argmax(result)] + ' with a score of ' + str(np.max(result) * 100)
    return outcome

uploaded_file = st.file_uploader('Upload an image')

if uploaded_file is not None:
    # Ensure the 'upload' directory exists
    os.makedirs('upload', exist_ok=True)
    
    # Save the uploaded file
    save_path = os.path.join('upload', uploaded_file.name)
    with open(save_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
 
    # Display the uploaded image
    st.image(uploaded_file, width=200)
    
    # Classify the uploaded image and display the result
    result = classify_images(save_path)
    st.markdown(result)
