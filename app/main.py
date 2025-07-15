from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ruta_inicial():
    return {"message" : "Hola mundo desde fastapi"}

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"message" : f"Homa, {nombre}"}