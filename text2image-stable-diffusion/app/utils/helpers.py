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
