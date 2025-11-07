from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Fridgedy API is working! 🍳"}

@app.get("/recipes/")
def get_recipes(ingredients: str):
    return {
        "ingredients": ingredients,
        "recipes": [
            "Nasi Goreng with your ingredients",
            "Curry Delight", 
            "Stir Fry Special"
        ]
    }
