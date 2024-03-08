import streamlit as st
import numpy as np
import cv2 as cv
from PIL import Image
import requests
import io
import base64
from time import sleep
import base64
# def autoplay_audio(file_path: str):
#     with open(file_path, "rb") as f:
#         data = f.read()
#         b64 = base64.b64encode(data).decode()
#         md = f"""
#             <audio autoplay="true">
#             <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
#             </audio>
#             """
#         st.markdown(
#             md,
#             unsafe_allow_html=True,
#         )
main_page = """
<style>
 @media screen{
    section {
        background-color : black;
        z-index : 0;
    }
    [data-testid="stCameraInputButton"] {
        width : 80vw;
        height: 100vh;
        z-index : 100;
        position: fixed;
        top: 0;
        left: 0;
        background-color : black;
    }
    video {
        z-index: 0;
        position: fixed;
        top : 10%;
        right: 0;
        width : 20vw;
        height: auto;


    }
    img {
        z-index: 0;
        position: fixed;
        top: 10%;
        right: 0;
        width : 20vw;
        height: auto;
    }
    }
</style>
"""
st.markdown(main_page, unsafe_allow_html=True)
def get_prediction(image_bytes):
    # Define the correct API endpoint URL
    url = "https://nfg-repo-rmhuz6i5bq-ew.a.run.app/predict"
    # Create an in-memory file-like object
    files = {'file': ('image.jpg', image_bytes, 'image/jpeg')}
    try:
        response = requests.post(url, files=files)
        if response.status_code == 200:
            # Assuming the server responds with JSON
            return response.json()
        else:
            return f"Error: Received status code {response.status_code}"
    except requests.RequestException as e:
        return f"Request failed: {e}"
picture = st.camera_input("")
# autoplay_audio(f"./audios/background_audio.mp3")
if picture:
    image = Image.open(io.BytesIO(picture.getvalue()))
    st.image(image, caption="Captured Image")
    # Convert the uploaded file to bytes for the request
    img_bytes = picture.getvalue()
    prediction = get_prediction(img_bytes)
    # Display the prediction result
    st.title(f"Votre plat est:{prediction['class']}")
    # st.audio(f"./audios/{prediction['class']}.mp3",autoplay=True)
    sleep(1)
    # autoplay_audio(f"./audios/{prediction['class']}.mp3")
