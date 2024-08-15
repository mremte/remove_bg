import streamlit as st
from PIL import Image
from rembg import remove
import io

# Title of the app
st.title("Remove Background from Image")

# Upload image
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Read image file
    image = Image.open(uploaded_file)

    # Display original image
    st.image(image, caption="Original Image", use_column_width=True)

    # Button to process the image
    if st.button("Remove Background"):
        # Remove background
        result = remove(image)

        # Display processed image
        st.image(result, caption="Processed Image", use_column_width=True)

        # Optionally, save the result to a file
        buf = io.BytesIO()
        result.save(buf, format="PNG")
        buf.seek(0)
        st.download_button(
            label="Download Processed Image",
            data=buf,
            file_name="processed_image.png",
            mime="image/png"
        )
