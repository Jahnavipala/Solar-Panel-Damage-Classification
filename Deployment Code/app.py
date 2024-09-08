import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os
import ultralytics

# Load the model
model_path = r"C:\Users\jahna\OneDrive\Desktop\SolarPanelDamageClassification\best.pt"
if os.path.exists(model_path):
    model = YOLO(model_path)
else:
    st.error(f"Model path '{model_path}' does not exist. Please check the path and try again.")

# Streamlit app
st.title('YOLO Object Detection')

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Detecting...")

    # Perform inference
    img_array = np.array(image)
    results = model(img_array)

    # Display results
    if results:
        for result in results:
            # result.plot() saves the image with bounding boxes to a temporary file
            result_img = result.plot()
            st.image(result_img, caption='Detected Image.', use_column_width=True)
    else:
        st.write("No detections were made.")
