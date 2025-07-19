import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# Set your Gemini API key
genai.configure(api_key="AIzaSyD0nSVTSD_l04VG0Vr0SSJCigDIy6uWekM")

# Title
st.set_page_config(page_title="🖼️ Image to Text with Gemini", layout="centered")
st.title("📸 Image Description using Gemini AI")
st.markdown("Upload an image and let Google's Gemini describe it!")

# Upload image
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

# Image prompt options
prompt_option = st.radio("What do you want?", ["Describe the image", "Extract any visible text"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Generate"):
        with st.spinner("Talking to Gemini..."):

            # Create model
            model = genai.GenerativeModel(model_name="gemini-pro-vision")

            # Prepare image as bytes
            img_bytes = io.BytesIO()
            image.save(img_bytes, format="PNG")
            img_bytes.seek(0)

            # Choose prompt
            prompt_text = "Describe the image in detail." if prompt_option == "Describe the image" else "Extract all the visible text from this image."

            # Generate response
            response = model.generate_content([prompt_text, img_bytes.read()], stream=False)

            st.subheader("🧠 Gemini AI Result:")
            st.markdown(response.text)
