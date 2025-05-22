from .model_loader import get_pipeline
from app.utils.helpers import save_image

def generate_image(prompt: str):
    pipe = get_pipeline()
    image = pipe(prompt, guidance_scale=7.5)["images"][0]
    path = save_image(image, prompt)
    return path
