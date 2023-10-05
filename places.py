import json


# função que pegas todas as opções de roteiro que a pessoa pode escolher
def get(): 
    with open("db/places.txt", "r", encoding="utf-8") as file:
        obj = json.loads(file.read())
        return obj['places']