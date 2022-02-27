import streamlit as st
from tensorflow.keras import models
import cv2
import numpy as np
from PIL import Image, ImageOps

st.set_option("deprecation.showfileUploaderEncoding", False)


@st.cache(allow_output_mutation=True)
def load_model():
    model = models.load_model("./Scanner/plant_disease_identification.hdf5")
    return model


def import_and_predict(image_data, model):
    size = (256, 256)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis, ...]
    predictions = model.predict(img_reshape)
    return predictions


st.title("Plant Disease Identification")

choice = st.selectbox("Choose an option", ["Scan", "Upload"])

if choice == "Upload":
    file = st.file_uploader(
        label="Select picture of plant disease",
        type=["jpg", "png"],
        accept_multiple_files=False,
    )
    if st.button("Search for plant disease"):
        if file is None:
            st.warning("Select an Image (png/jpg) to continue. ")
        else:
            image = Image.open(file)
            model = load_model()
            st.image(image, use_column_width=True)
            predictions = import_and_predict(image, model)
            class_names = [
                "Bacterial Spots",
                "Healthy",
                "Early Blight",
                "Healthy",
                "Late Blight",
                "Target Spots",
                "Mosaic Virus",
                "Yellow Leaf Curl Virus",
                "Bacterial Spots",
                "Early Blight",
                "Healthy",
                "Late Blight",
                "Leaf Mold",
                "Leaf Spots",
                "Spider Mites"
            ]

            disease = class_names[np.argmax(predictions)]

            if disease == "Healthy":
                st.success("This crop looks disease free!")
            else:
                st.warning("This disease looks like", disease)
else:
    file = st.camera_input("Click a picture of plant disease.")
    if st.button("Search for plant disease"):
        if file is None:
            st.warning("Select an Image (png/jpg) to continue.")
        else:
            image = Image.open(file)
            model = load_model()
            st.image(image, use_column_width=True)
            predictions = import_and_predict(image, model)
            st.success("There is no disease on this plant.")
