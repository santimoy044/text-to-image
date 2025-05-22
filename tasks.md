✅ MVP Build Plan — Text-to-Image (Stable Diffusion + Python + Diffusers)

🔹 PHASE 1: Setup & Environment

Task 1: Create project folder structure
Start: Make base directory and subfolders
End: File structure exists as per architecture
mkdir -p text2image-stable-diffusion/{app/services,app/utils,static/outputs}
touch text2image-stable-diffusion/{app/__init__.py,app/main.py,app/routes.py,app/services/__init__.py,app/services/image_generator.py,app/services/model_loader.py,app/utils/__init__.py,app/utils/helpers.py,config.py,.env,requirements.txt,run.py}

Task 2: Initialize virtual environment and install base dependencies
Start: Run virtual env command
End: Environment activated and requirements.txt filled
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn torch diffusers transformers Pillow python-dotenv
pip freeze > requirements.txt

Task 3: Add a simple FastAPI app and run it
Start: Add a Hello World endpoint to main.py
End: Accessible at http://localhost:8000
# app/main.py
from fastapi import FastAPI
from app.routes import router

app = FastAPI()
app.include_router(router)
# app/routes.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Text-to-Image API is running!"}

🔹 PHASE 2: Model Loading Service

Task 4: Implement config values for model and device
Start: Create config.py
End: Returns model name and device type from .env
# config.py
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "CompVis/stable-diffusion-v1-4")
DEVICE = os.getenv("DEVICE", "cuda")
OUTPUT_DIR = "static/outputs"

Task 5: Load Stable Diffusion model in a service
Start: Write get_pipeline() in model_loader.py
End: Returns a cached instance of the model
# app/services/model_loader.py
from diffusers import StableDiffusionPipeline
import torch
from config import MODEL_NAME, DEVICE

pipe = None

def get_pipeline():
    global pipe
    if pipe is None:
        pipe = StableDiffusionPipeline.from_pretrained(MODEL_NAME, torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32)
        pipe = pipe.to(DEVICE)
    return pipe

🔹 PHASE 3: Image Generation Logic

Task 6: Generate an image from a static prompt
Start: Add generate_image(prompt) function
End: Returns PIL image from prompt
# app/services/image_generator.py
from .model_loader import get_pipeline

def generate_image(prompt: str):
    pipe = get_pipeline()
    result = pipe(prompt, guidance_scale=7.5)
    return result["images"][0]

Task 7: Save image to output directory
Start: Add save_image() helper
End: Saves image to static/outputs/, returns path
# app/utils/helpers.py
from PIL import Image
import os
from datetime import datetime
from config import OUTPUT_DIR

def save_image(image: Image.Image, prompt: str) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}.png"
    path = os.path.join(OUTPUT_DIR, filename)
    image.save(path)
    return path

Task 8: Connect generation + saving logic
Start: Update generate_image() to save and return file path
End: Returns image path string
# app/services/image_generator.py
from app.utils.helpers import save_image

def generate_image(prompt: str):
    pipe = get_pipeline()
    image = pipe(prompt, guidance_scale=7.5)["images"][0]
    path = save_image(image, prompt)
    return path

🔹 PHASE 4: API Route

Task 9: Create POST /generate endpoint
Start: Add POST endpoint for JSON body with prompt
End: Returns image path as response
# app/routes.py
from fastapi import APIRouter, Request
from app.services.image_generator import generate_image

router = APIRouter()

@router.post("/generate")
async def generate(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    if not prompt:
        return {"error": "Prompt is required"}
    image_path = generate_image(prompt)
    return {"image_path": image_path}

🔹 PHASE 5: Testing & Validation

Task 10: Test image generation with a sample prompt
Start: Run the app with uvicorn
End: Send POST request, get image path
uvicorn run:app --reload
POST Request:
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "a fantasy castle on a mountain"}'
Expected Response:
{
  "image_path": "static/outputs/20250521123000.png"
}

🔹 PHASE 6: Optional Enhancements
These are outside MVP, but simple to queue up next:
    • ✅ Return base64 instead of path
    • ✅ Serve static images from /static/outputs/
    • ✅ Add Gradio or Streamlit frontend
    • ✅ Dockerize the project
    • ✅ Add prompt validation and error handling
