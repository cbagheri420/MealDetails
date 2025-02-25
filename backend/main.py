from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "your_api_key"  # Replace with your Spoonacular API key

@app.post("/get-nutrition")
def get_nutrition(food: str):
    url = f"https://api.spoonacular.com/food/ingredients/search?query={food}&apiKey={API_KEY}"
    response = requests.get(url)
    return response.json()