from fastapi import FastAPI
import uvicorn
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    menu: str = None

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    return "Hello World"




@app.post("/fetch")
async def fetch(request: Request):
    param = await request.json()
    print(param['menu'])
    return JSONResponse(content={'result':'success'})

@app.post("/fetch_bm")
async def fetch_bm(item:Item):
    print(item.menu)
    return JSONResponse(content={'result':'success'})


@app.post("/axios")
async def axios(request: Request):
    param = await request.json()
    print(param['menu'])
    return JSONResponse(content={'result':'success'})

@app.post("/ajax")
async def ajax(menu: str = Form()):
    print(menu)
    return JSONResponse(content={'result':'success'})

@app.post("/ajax2")
async def ajax2(request: Request):
    param = await request.json()
    print(param['menu'])
    return JSONResponse(content={'result':'success'})



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    
    
    