from fastapi import FastAPI
from app.routers import match

app = FastAPI()
app.include_router(match.router)



# @app.get("/") # This called by router decorator. means that if someone send get request to the website, the function of under line of the app.get router decorator will be executed. 
# def read_root():
#     return {"message": "Hello, House of Legends!"}
