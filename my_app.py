import streamlit as st
from ocr import OCR
def main():
  uploaded_file = st.file_uploader("Choose an Image", type=['jpg', 'png', 'jpeg'])

  if uploaded_file is not None:
    # Read the uploaded image as bytes
    image_bytes = uploaded_file.read()

    st.image(image_bytes, width=250)

  user_input = st.text_input("Enter your text here")

  st.write("Text output will be displayed here after processing.")

  # Add a button or other mechanism to trigger processing if needed
  # This section depends on your specific processing logic

  # Example processing (replace with your actual logic)
  if st.button("Process Text"):
    processed_text = user_input.upper()  # Simple uppercase conversion (modify as needed)
    st.write("Processed Text:", processed_text)

if __name__ == "__main__":
  ocr = OCR()
  image_path = r"C:\Users\pshen\Downloads\dolo650.jpg"
  ocr.get_medicine_name(image_path)
  data=ocr.get_medicine_name(image_path)
  print(data)
medicine_names = [medicine[0]['name'] for medicine in data]
        for name in medicine_names:
            st.write(name)