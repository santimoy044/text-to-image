import requests
import os
from PIL import Image
import json

def test_api():
    # Test the root endpoint
    response = requests.get("http://localhost:8000/")
    assert response.status_code == 200
    assert response.json()["message"] == "Text-to-Image API is running!"
    print("✅ Root endpoint test passed")

    # Test the generate endpoint
    prompt = "a fantasy castle on a mountain"
    response = requests.post(
        "http://localhost:8000/generate",
        json={"prompt": prompt}
    )
    assert response.status_code == 200
    data = response.json()
    assert "image_path" in data
    print("✅ Generate endpoint test passed")

    # Verify the image file exists
    image_path = data["image_path"]
    assert os.path.exists(image_path)
    print(f"✅ Image file exists at: {image_path}")

    # Verify the image is valid
    try:
        with Image.open(image_path) as img:
            print(f"✅ Image is valid (size: {img.size})")
    except Exception as e:
        print(f"❌ Error opening image: {str(e)}")
        return False

    return True

if __name__ == "__main__":
    print("Starting API tests...")
    if test_api():
        print("All tests passed! 🎉")
    else:
        print("Tests failed! ❌") 