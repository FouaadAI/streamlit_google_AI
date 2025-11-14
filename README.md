# Streamlit Google AI — Image Questioning App

A Streamlit-powered application that allows users to upload or link an image, ask intelligent questions about it, and receive AI-generated responses using **Google Gemini (Generative AI)**.
The app also saves all interactions and offers a history download feature.

Live App:
**[https://fou-ask-ai.streamlit.app/](https://fou-ask-ai.streamlit.app/)**

---

## Features

* **Image Input Options**

  * Upload an image (JPG, PNG, JPEG)
  * Fetch an image directly via URL

* **AI-Powered Image Understanding**

  * Ask any question about the uploaded image
  * Powered by **Google Gemini 2.0 Flash**

* **Interaction Saving**

  * Saves: image URL, question, and AI answer
  * Stores data in a structured JSON file

* **History Panel**

  * View the last 5 interactions in the sidebar
  * Display past images, questions, and answers

* **Download Interaction History**

  * Export all saved data as `saved_data.json`

* **Summarization**

  * Summarize long AI answers instantly

---

## Project Structure

```
streamlit_google_AI/
│
├── app.py                 # Main Streamlit application
├── saved_data.json        # Auto-generated interaction history
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── other project files...
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/FouaadAI/streamlit_google_AI.git
cd streamlit_google_AI
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Your Google API Key

Inside `app.py`, replace:

```python
GOOGLE_API_KEY = "YOUR_API_KEY"
```

with your actual key.

---

## Usage

### Start the App

```bash
streamlit run app.py
```

### How It Works

1. Enter an image URL **or** upload an image.
2. Type a question about the image.
3. Press **Process** to get the AI response.
4. View saved interactions from the sidebar.
5. Download interaction history anytime.
6. Use **Summarize Answer** for short summaries.

---

## Requirements

Include these in `requirements.txt`:

```
streamlit
Transformers
tensorflow
torch
google-generativeai
Pillow
requests
```

---

## Technologies Used

| Technology           | Purpose                               |
| -------------------- | ------------------------------------- |
| **Streamlit**        | Web application framework             |
| **Google Gemini AI** | Image + text generative model         |
| **PIL (Pillow)**     | Image processing                      |
| **Requests**         | Fetch images from URLs                |
| **JSON**             | Saving and loading past conversations |

---

## Live Demo

Access the full working application here:

**[https://fou-ask-ai.streamlit.app/](https://fou-ask-ai.streamlit.app/)**

---

## License

This project is MIT licensed. Modify and use freely.

---
