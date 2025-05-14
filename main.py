import streamlit as st
import requests
import PIL
from PIL import Image
from io import BytesIO
import google.generativeai as genai
import json

# Configure API Key for Google Generative AI
GOOGLE_API_KEY = 'AIzaSyCuiusvKu9OU1pSEj-91z31NkSJsqwzn2s'  # Replace with your API key
genai.configure(api_key=GOOGLE_API_KEY)
vision_model = genai.GenerativeModel('gemini-2.0-flash')

st.title("Chat with Graphs APP")
st.write("Upload an image or provide a URL, then ask questions about it. The app processes the image using AI and generates responses.")

# Function to fetch image from URL
@st.cache_data
def fetch_image(image_url):
    result = requests.get(image_url)
    try:
        image = PIL.Image.open(BytesIO(result.content))
        return image
    except PIL.UnidentifiedImageError:
        st.error("Error: Unidentified image format.")
        return None

# Function to save the questions, answers, and image URL
def save_interaction(image_url, question, answer, filename="saved_data.json"):
    data = {"image_url": image_url, "question": question, "answer": answer}

    # Load existing data if the file exists
    try:
        with open(filename, "r") as file:
            saved_data = json.load(file)
    except FileNotFoundError:
        saved_data = []

    # Append new interaction
    saved_data.append(data)

    # Save back to file
    with open(filename, "w") as file:
        json.dump(saved_data, file, indent=4)

# Function to load saved interactions
def load_interactions(filename="saved_data.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Main function for the Streamlit app
def main():
    st.sidebar.subheader("Choose an Image Source")

    # Initialize image variable
    image = None

    # Image URL input
    image_url = st.sidebar.text_input("Enter Image URL:")
    
    # Upload image option
    uploaded_image = st.sidebar.file_uploader("Or Upload an Image", type=["jpg", "png", "jpeg"])

    if image_url:
        image = fetch_image(image_url)
    elif uploaded_image is not None:
        image = Image.open(uploaded_image)
        image_url = "Uploaded Image"

    if image:
        st.sidebar.image(image, caption="Selected Image", use_container_width=True)

    st.write("Ask any query about the image:")
    user_input = st.text_input("Your Query:")

    if st.button("Process") and user_input:
        response = vision_model.generate_content([user_input, image])
        answer_text = response.text
        st.text_area("Model's Response:", value=answer_text, height=200)

        save_interaction(image_url, user_input, answer_text)
        st.success("Interaction saved successfully!")

    # Display previous interactions
    st.sidebar.subheader("Past Interactions")
    saved_interactions = load_interactions()

    if saved_interactions:
        for interaction in saved_interactions[-5:]:
            if interaction["image_url"] != "Uploaded Image":
                st.sidebar.image(interaction["image_url"], caption="Previous Image", use_container_width=True)
            st.sidebar.write(f"**Question:** {interaction['question']}")
            st.sidebar.write(f"**Answer:** {interaction['answer']}")
            st.sidebar.write("---")

    # Allow users to download their interaction history
    if saved_interactions:
        saved_data = json.dumps(saved_interactions, indent=4)
        st.download_button(label="Download History", data=saved_data, file_name="saved_data.json", mime="application/json")

    # Summarize AI Response
if st.button("Summarize Answer"):
    if 'answer_text' in locals():  # Check if answer_text is defined
        summary = vision_model.generate_content(["Summarize this:", answer_text])
        st.text_area("Summarized Response:", value=summary.text, height=150)
    else:
        st.error("Please process the image and query first before summarizing.")

if __name__ == "__main__":
    main()