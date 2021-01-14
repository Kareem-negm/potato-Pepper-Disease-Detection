import cv2
import streamlit as st
import tensorflow as tf
from PIL import Image ,ImageOps
import numpy as np
 

drive_weighs_URL='https://drive.google.com/file/d/1MRTBcbOspufLSH4blKpbxmvZ217j6KLI/view?usp=sharing'
@st.cache(allow_output_mutation=True)
def load_model():
    model=tf.keras.models.load_model(drive_weighs_URL+'my_model_weights.hdf5')
    return model

model=load_model()
st.write("""
# Plant Disease Detection

""")

file=st.file_uploader("pleas upload an plant image",type=["jpg","png"])

def import_and_predict(image_data , model):
    size(256,256)
    image = ImageOps.fit(image_data,size,Image.ANTIALIAS)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(imge_reshape)
    return prediction



if file is None:
    st.text("pleas uplod an image file ")
else:
    imge=Image.open(file)
    st.image(image,use_column_width=True)
    predictions=import_and_predict(imge,model)
    class_names=['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
    string="this imge most likely is:"+class_names[np.argmax(predictions)]
    st.success(srting)
