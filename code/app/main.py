from fastapi import FastAPI
from Routers import data, saveSortedData

app = FastAPI()

app.include_router(data.router)
app.include_router(saveSortedData.router)

@app.get('/')
def root():
    return "hello Eazel!"
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/")
# async def read_item(search: str, limit: int):
#     print(f'search: {parse.unquote(search)}')
#     print(f'limit: {limit}')
