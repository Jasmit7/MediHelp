import streamlit as st
import os
from ocr import OCR
import json
from webScrap import medicineDesc

def main():
    ocr = OCR()
    st.title("Medicine Information Extractor")

    st.sidebar.subheader("Upload an Image")
    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image_path = save_uploaded_file(uploaded_file)
        
        # Displaying the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True, width=250)  # Adjust width as needed
        
        # Getting medicine information
        data = ocr.get_medicine_name(image_path)
        
        st.subheader("Extracted Medicine Data")
        for medicine_info, _, _ in data:
            st.write("### Name:", medicine_info["name"])
            st.write("**Synonyms:**", ", ".join(medicine_info["synonyms"]))
            st.write("**Medline Plus ID:**", medicine_info.get("medline_plus_id", "Not available"))
            st.write("**Mesh ID:**", medicine_info.get("mesh_id", "Not available"))
            st.write("**Drugbank ID:**", medicine_info.get("drugbank_id", "Not available"))
            st.write("**Description:**", medicineDesc(medicine_info["name"].lower()))
            st.markdown("---")

def save_uploaded_file(uploaded_file):
    if not os.path.exists("uploaded_images"):
        os.makedirs("uploaded_images")
    
    image_path = os.path.join("uploaded_images", uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return image_path

if __name__ == "__main__":
    main()
