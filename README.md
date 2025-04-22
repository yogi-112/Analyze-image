# 🎉 AI-Powered Birthday Wish Generator using Gemini on Vertex AI

This project demonstrates how to use **Google Cloud Vertex AI** with the **Gemini multimodal model** to generate personalized birthday wishes from an image.

Give the model a picture of a bouquet, cake, or party scene—and let it create a thoughtful birthday message based on what it "sees"!

---
## 📸 What It Does

✅ Loads an image file  
✅ Sends it to the **Gemini 2.0 Flash model** via Vertex AI  
✅ Asks the model to generate a creative birthday wish based on the image  
✅ Prints the AI-generated result ✨

---
## 🧠 Powered By

- [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai)
- [Gemini 2.0 Flash Model](https://cloud.google.com/vertex-ai/docs/generative-ai/overview)
- Python 3
- `vertexai` SDK

---
## 📂 Project Structure
 ├── image.jpeg # Input image (e.g., flower bouquet) ├── main.py # Python script with AI generation logic ├── README.md # This file
---
## 🚀 Getting Started

### 1. Set up Google Cloud Vertex AI

- Enable Vertex AI API
- Create a service account with necessary permissions
- Authenticate with `gcloud auth application-default login`

### 2. Install the Vertex AI SDK
```bash
pip install google-cloud-aiplatform

3. Run the Script
Update main.py with your project ID and region:
project_id = "your-gcp-project-id"
location = "your-region"

