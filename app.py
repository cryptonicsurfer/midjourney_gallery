import streamlit as st
import os

# Read the filenames.txt and split it into filenames and captions
with open("filenames.txt", 'r') as f:
    lines = f.readlines()
    # Split based on the first comma
    image_files = [line.split(',', 1)[0].strip() for line in lines]
    captions = [line.split(',', 1)[1].strip() for line in lines]

# Streamlit App
st.title("Midjourney exempelbilder med prompts")

# Display images with captions
for i, img_file in enumerate(image_files):
    img_path = os.path.join("images", img_file)  
    if os.path.exists(img_path):
        image = st.image(img_path, use_column_width=True)
        st.caption(captions[i])
    else:
        st.write(f"Image {img_file} not found!")

