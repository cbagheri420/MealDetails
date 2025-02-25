from fastapi import FastAPI, HTTPException
import requests
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI()

# CORS middleware to allow cross-origin requests (important for local development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],  # allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # allow all headers
)

# Serve static files (index.html, styles.css, scripts.js)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Spoonacular API key (replace with your actual key)
API_KEY = "your_api_key_here"  # Replace with your actual API key

@app.get("/")
def read_root():
    return {"message": "Welcome to the Nutrition Analyzer!"}

@app.post("/get-nutrition")
def get_nutrition(food: str):
    # Construct the API request to Spoonacular
    url = f"https://api.spoonacular.com/food/ingredients/search?query={food}&apiKey={API_KEY}"
    response = requests.get(url)

    # If the request fails, raise an HTTP error
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, 
            detail="Error fetching nutrition data from Spoonacular API."
        )

    # Return the API response as JSON
    return response.json()