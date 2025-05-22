🖼️ Text-to-Image Generator with Stable Diffusion (using diffusers)
📁 Project Structure
text2image-stable-diffusion/
├── app/
│   ├── __init__.py
│   ├── main.py                # Entry point (Flask/FastAPI app)
│   ├── routes.py              # API route(s)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── image_generator.py # Core Stable Diffusion generation logic
│   │   └── model_loader.py    # Loads and caches the model
│   └── utils/
│       ├── __init__.py
│       └── helpers.py         # Helper functions (file saving, prompt cleaning, etc.)
├── static/
│   └── outputs/               # Generated images are stored here
├── requirements.txt           # Project dependencies
├── config.py                  # Config for model name, device, etc.
├── .env                       # Secrets and environment variables
├── README.md                  # Project documentation
└── run.py                     # Script to run the app

🧠 Overview of Components
1. app/main.py
    • Starts the web app (using FastAPI or Flask).
    • Includes app-level configuration and middleware.
    • Imports and registers routes.
2. app/routes.py
    • Defines REST endpoints.
    • /generate endpoint takes a prompt and returns the image URL or base64 string.
3. app/services/model_loader.py
    • Loads and caches the Stable Diffusion model (StableDiffusionPipeline).
    • Ensures model is loaded only once (singleton or module-level caching).
    • Configurable for cpu / cuda or mps.
4. app/services/image_generator.py
    • Calls the pipeline loaded in model_loader.py.
    • Accepts prompt and other parameters (guidance scale, num inference steps).
    • Saves the generated image to disk or returns as base64.
    • Handles post-processing (e.g., resizing or enhancement if needed).
5. app/utils/helpers.py
    • Cleans input prompt.
    • Generates filenames, timestamps.
    • Converts images to base64 (if required).
    • Logging or timing utilities.
6. static/outputs/
    • Stores generated images.
    • You can serve them statically via FastAPI or Flask.
7. config.py
    • Stores model settings:
      MODEL_NAME = "CompVis/stable-diffusion-v1-4"
      DEVICE = "cuda"  # or "cpu", "mps"
      OUTPUT_DIR = "static/outputs"
8. .env
    • Holds secret keys, debug flags, etc.

🗺️ Flow: How It Works
graph TD
    A[User submits prompt] --> B[FastAPI endpoint /generate]
    B --> C[image_generator.py - generate()]
    C --> D[model_loader.py - get_pipeline()]
    D --> E[Loads StableDiffusionPipeline]
    C --> F[Generate image using pipeline]
    F --> G[Save to static/outputs or return base64]
    G --> H[Return image URL or base64 to user]

🧬 Where State Lives
Component
State Type
Description
model_loader.py
Model instance (singleton)
The Stable Diffusion pipeline (cached model)
image_generator.py
Stateless per request
Uses loaded model to generate per prompt
static/outputs/
File system
Stores persistent generated images
config.py / .env
App config
Device, model name, and environment settings

🔗 Service Interactions
From
To
Purpose
routes.py
image_generator.py
Calls generation function
image_generator.py
model_loader.py
Loads and caches the model
image_generator.py
helpers.py
Image saving, prompt cleaning, etc.

🧪 Example Endpoint Flow (FastAPI)
# app/routes.py
from fastapi import APIRouter, Request
from app.services.image_generator import generate_image

router = APIRouter()

@router.post("/generate")
async def generate(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    image_path = generate_image(prompt)
    return {"image_url": image_path}

📦 Example: generate_image function
# app/services/image_generator.py
from .model_loader import get_pipeline
from app.utils.helpers import save_image
import torch

def generate_image(prompt: str):
    pipeline = get_pipeline()
    image = pipeline(prompt, guidance_scale=7.5)["images"][0]
    path = save_image(image, prompt)
    return path

🧩 Libraries Used
    • transformers, diffusers, torch, Pillow
    • FastAPI or Flask (for API)
    • python-dotenv (for config)
    • uvicorn (if FastAPI)

📄 requirements.txt
torch
diffusers
transformers
Pillow
fastapi
uvicorn
python-dotenv

✅ Example .env
DEVICE=cuda
DEBUG=True

✅ Example config.py
import os

MODEL_NAME = "CompVis/stable-diffusion-v1-4"
DEVICE = os.getenv("DEVICE", "cuda")
OUTPUT_DIR = "static/outputs"

✅ Run the App
# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn run:app --reload

🧠 Tips
    • Use fp16 model for performance if using GPU.
    • Cache model loading with @lru_cache() or module-level variable.
    • You can optionally use a frontend (React/Vite) to submit prompts via HTTP.

Let me know if you'd like this with:
    • ✅ Frontend UI in React
    • ✅ Docker setup
    • ✅ Streamlit or Gradio interface
