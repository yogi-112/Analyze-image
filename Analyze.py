import vertexai
from vertexai.generative_models import GenerativeModel, Part, Image

def analyze_bouquet_image(project_id: str, location: str) -> str:
    vertexai.init(project=project_id, location=location)
    multimodal_model = GenerativeModel("gemini-2.0-flash-001")
    response = multimodal_model.generate_content(
        [Part.from_image(Image.load_from_file("image.jpeg")), "Generate birthday wishes based on this image?",])
    return response.text

project_id = "$PROJECT_ID"
location = "$REGION"

response = analyze_bouquet_image(project_id, location)
print(response)
