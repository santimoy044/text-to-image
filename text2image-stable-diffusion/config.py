import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "CompVis/stable-diffusion-v1-4")
DEVICE = os.getenv("DEVICE", "cuda")
OUTPUT_DIR = "static/outputs"
