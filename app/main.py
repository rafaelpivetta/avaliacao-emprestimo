from fastapi import FastAPI
from sklearn.pipeline import Pipeline
import joblib
from pydantic import BaseModel
import pandas as pd

# Definir o modelo de dados de entrada usando Pydantic
class LoanRequest(BaseModel):
    Age: int
    Annual_Income: float
    Credit_Score: int
    Employment_Years: float
    Loan_Amount_Requested: float

app = FastAPI()

# Carregar a pipeline do arquivo .joblib 
loaded_pipeline = joblib.load('loan_default_pipeline.joblib')

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao modelo de avaliacao de emprestimo!!"}

# Definir a rota de predição aceitando um dicionário diretamente
@app.post("/predict")
def predict(data: LoanRequest):
    # Converter os dados de entrada para um DataFrame

    input_data = pd.DataFrame([data.dict().values()], columns=data.dict().keys())
    
    # Fazer a predição usando a pipeline carregada
    prediction = loaded_pipeline.predict_proba(input_data)[:, 1][0]
    
    return {"probabilidade_default": prediction}