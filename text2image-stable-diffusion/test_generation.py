from app.services.image_generator import generate_image

def test_generation():
    prompt = "a fantasy castle on a mountain"
    try:
        # Generate and save image
        saved_path = generate_image(prompt)
        print("Image generated and saved successfully!")
        print(f"Image saved to: {saved_path}")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_generation() 