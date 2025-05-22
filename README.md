# Text-to-Image Generator with Stable Diffusion

A FastAPI-based application that generates images from text prompts using the Stable Diffusion model.

## 🚀 Features

- Text-to-image generation using Stable Diffusion
- RESTful API endpoints for image generation
- Automatic model caching for faster subsequent generations
- Configurable generation parameters
- Image saving and retrieval functionality

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/santimoy044/text-to-image.git
cd text-to-image/text2image-stable-diffusion
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

1. Create a `.env` file in the project root:

```bash
DEVICE=cuda  # or "cpu" if no GPU available
DEBUG=True
```

2. The first time you run the application, it will download the Stable Diffusion model (several GB).

## 🚀 Running the Application

1. Start the FastAPI server:

```bash
python run.py
```

2. The server will start at `http://localhost:8000`

## 📝 API Endpoints

### 1. Root Endpoint

- **URL**: `/`
- **Method**: `GET`
- **Response**: Status message

```bash
curl http://localhost:8000
```

### 2. Generate Image

- **URL**: `/generate`
- **Method**: `POST`
- **Body**:

```json
{
  "prompt": "your text description here"
}
```

- **Example**:

```bash
curl -X POST http://localhost:8000/generate \
-H "Content-Type: application/json" \
-d '{"prompt": "a beautiful sunset over mountains"}'
```

## 📁 Project Structure

```
text2image-stable-diffusion/
├── app/
│   ├── main.py                # FastAPI application
│   ├── routes.py              # API endpoints
│   ├── services/
│   │   ├── image_generator.py # Image generation logic
│   │   └── model_loader.py    # Model loading and caching
│   └── utils/
│       └── helpers.py         # Utility functions
├── static/
│   └── outputs/              # Generated images
├── requirements.txt          # Project dependencies
├── config.py                # Configuration settings
└── run.py                   # Application entry point
```

## 🧪 Testing

Run the test scripts:

```bash
python test_api.py
python test_generation.py
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

Santimoy - [@santimoy044](https://github.com/santimoy044)

Project Link: [https://github.com/santimoy044/text-to-image](https://github.com/santimoy044/text-to-image)
