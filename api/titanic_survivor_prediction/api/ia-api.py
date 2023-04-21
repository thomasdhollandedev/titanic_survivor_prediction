from fastapi import FastAPI, Body
import pickle
import pandas as pd

# Chargez votre modèle de prédiction à partir du fichier model.pkl
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Créer une instance FastAPI
app = FastAPI()

# Définir une route pour l'API qui effectue une prédiction de survie à partir des données de l'utilisateur
@app.post("/predict")
async def predict_survival(body: dict = Body(...)):
    
    Age = int(body['Age'])
    Fare = int(body['Fare'])
    FamilySize = int(body['FamilySize'])
    Pclass = int(body['Pclass'])
    Sex_male = int(body['Sex_male'])
    Embarked_Q = int(body['Embarked_Q'])
    Embarked_S = int(body['Embarked_S'])
    
    X = pd.DataFrame([[Age, Fare, FamilySize, Pclass, Sex_male, Embarked_Q, Embarked_S]], columns = ['Age', 'Fare', 'FamilySize', 'Pclass', 'Sex_male','Embarked_Q', 'Embarked_S'])
    print(X)
    proba = model.predict_proba(X.head(1))
    print(proba)
    return {"survival_probability": round(float(proba[0][1]), 2)}