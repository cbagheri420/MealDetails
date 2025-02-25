from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Replace with your actual Spoonacular API key
API_KEY = "your_actual_api_key"

@app.post("/get-nutrition")
def get_nutrition(food: str):
    url = f"https://api.spoonacular.com/food/ingredients/search?query={food}&apiKey={API_KEY}"
    response = requests.get(url)
    
    # Check if the API request was successful
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, 
            detail="Error fetching nutrition data from Spoonacular API."
        )
    
    # Return the API response as JSON
    return response.json()