import cv2
import numpy as np
import os
import streamlit as st
from PIL import Image
import datetime  # Import the datetime module

# Set page config with a title and favicon
st.set_page_config(
    page_title="Enhance picture",
    page_icon=":robot:",
)

# --- Input and Output Folders ---
input_folder = 'sumber'  # Replace with your input folder path
output_folder = 'hasil'   # Replace with your output folder path

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# --- Image Processing Function ---
def process_image(img):
    """Processes a single image and returns the enhanced images."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl1 = clahe.apply(gray)
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened = cv2.filter2D(img, -1, kernel)
    return equ, cl1, sharpened

def analyze_rgb(img):
    """Analyzes the RGB channels of an image and returns the mean values."""
    r_channel = img[:, :, 0]
    g_channel = img[:, :, 1]
    b_channel = img[:, :, 2]

    r_mean = np.mean(r_channel)
    g_mean = np.mean(g_channel)
    b_mean = np.mean(b_channel)

    return r_mean, g_mean, b_mean

# --- Streamlit Application ---
st.title("Image Enhancer")
st.write("Upload your images for enhancement.")

uploaded_files = st.file_uploader("Choose images...", accept_multiple_files=True, type=["jpg", "png", "jpeg"])

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Read image with PIL
        image = Image.open(uploaded_file)
        img_np = np.array(image)

        # Process the image
        equ, cl1, sharpened = process_image(img_np)

        # Analyze RGB channels for original image
        r_mean_original, g_mean_original, b_mean_original = analyze_rgb(img_np)

        # Analyze RGB channels for sharpened image
        r_mean_sharpened, g_mean_sharpened, b_mean_sharpened = analyze_rgb(sharpened)

        # Display original and processed images
        st.subheader(f"Original: {uploaded_file.name}")
        st.image(img_np, channels="BGR", use_container_width=True)
        st.write(f"RGB Analysis: Red={r_mean_original:.2f}, Green={g_mean_original:.2f}, Blue={b_mean_original:.2f}")

        st.subheader(f"Equalized Histogram: {uploaded_file.name}")
        st.image(equ, use_container_width=True, clamp=True)

        st.subheader(f"CLAHE: {uploaded_file.name}")
        st.image(cl1, use_container_width=True, clamp=True)

        st.subheader(f"Sharpened: {uploaded_file.name}")
        st.image(sharpened, channels="BGR", use_container_width=True)
        st.write(f"Sharpened RGB Analysis: Red={r_mean_sharpened:.2f}, Green={g_mean_sharpened:.2f}, Blue={b_mean_sharpened:.2f}")

# Remove the if __name__ == '__main__': block and call main() directly
current_year = datetime.datetime.now().year

# Footer
st.markdown(f"""
<div style="text-align: center; padding-top: 20px;">
    © {current_year} Developed by: Galuh Adi Insani. All rights reserved.
</div>
""", unsafe_allow_html=True)

hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_st_style, unsafe_allow_html=True)