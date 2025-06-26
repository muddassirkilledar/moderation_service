import requests
import os
from dotenv import load_dotenv


load_dotenv()

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/unitary/toxic-bert"
HUGGINGFACE_API_KEY = os.getenv("HF_API_TOKEN")


def check_toxicity(text):
    if not HUGGINGFACE_API_KEY:
        raise ValueError("Missing Hugging Face API key")

    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    response = requests.post(
        HUGGINGFACE_API_URL,
        headers=headers,
        json={"inputs": text}
    )

    if response.status_code != 200:
        return False, {}

    try:
        result = response.json()
        print("Hugging Face API response:", result)  

    except Exception:
        return False, {}

    # Handle Hugging Face error structure
    if isinstance(result, dict) and result.get("error"):
        return False, {}

    toxic_categories = {
        label["label"]: label["score"]
        for label in result[0]
        if label["score"] > 0.5
    }

    return bool(toxic_categories), toxic_categories