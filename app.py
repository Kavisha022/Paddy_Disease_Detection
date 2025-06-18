import streamlit as st
import json
from utils.predict import predict_disease
import os

# # Load disease sinhala.json
# with open("disease_info/sinhala.json", "r", encoding='utf-8') as f:
#     disease_data = json.load(f)

# Load disease english.json
with open("disease_info/english.json", "r", encoding='utf-8') as f:
    disease_data = json.load(f)

st.set_page_config(page_title="Paddy Disease Detector", layout="centered")
st.title("🌾 Paddy Disease Detector")
st.write("Upload an image of a paddy leaf to detect the disease and get the solution.")

# st.set_page_config(page_title="වියළි සහිත රෝග හඳුනාගැනීම", layout="centered")
# st.title("🌾 පෝෂ්‍ය රෝග හඳුනාගැනීම")
# st.write("ඔබගේ නව පදම අස්වනු තැඹිලි පත්‍ර රූපයක් උඩුගත කර එහි ඇති රෝගය හා විසඳුම ලබා ගන්න.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    file_path = f"temp_image.jpg"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(file_path, caption="Uploaded Image", use_column_width=True)

    # Predict disease
    label = predict_disease(file_path)

    # Display In English
    st.success(f"🩺 Detected Disease: **{label}**")
    if label in disease_data:
        st.markdown(f"**📌 Reason:** {disease_data[label]['reason']}")
        st.markdown(f"**🧪 Solution:** {disease_data[label]['solution']}")
    else:
        st.warning("No additional information available for this disease.")

    # Display in sinhala
    # st.success((f"🩺 රෝගය: **{label}**"))
    # if label in disease_data:
    #     st.markdown(f"**📌 හේතුව:** {disease_data[label]['reason']}")
    #     st.markdown(f"**🧪 විසඳුම:** {disease_data[label]['solution']}")
    # else:
    #     st.warning("මෙම රෝගය සඳහා තොරතුරු නොමැත.")


    os.remove(file_path)
