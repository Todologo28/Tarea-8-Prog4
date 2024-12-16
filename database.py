# database.py
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Tarea5"]
recipes_collection = db["recetas"]

def get_recipes():
    return list(recipes_collection.find())

def add_recipe(name, ingredients, steps):
    recipe = {
        "name": name,
        "ingredients": ingredients,
        "steps": steps
    }
    recipes_collection.insert_one(recipe)
