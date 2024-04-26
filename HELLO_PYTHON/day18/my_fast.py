from fastapi import FastAPI
import uvicorn
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from day18.dao_mem import DaoMem
from starlette.responses import RedirectResponse


templates = Jinja2Templates(directory="templates")

class Mem(BaseModel):
    m_id: str = None
    m_name: str = None
    tel: str = None
    email: str = None

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    return  RedirectResponse("/static/mem.html")


@app.post("/mem_list")
async def mem_list():
    dm = DaoMem()
    list = dm.selectList()
    return JSONResponse(content={'list':list})

@app.post("/mem_select")
async def mem_select(mem:Mem):
    dm = DaoMem()
    vo = dm.select(mem.m_id)
    return JSONResponse(content={'vo':vo})

@app.post("/mem_insert")
async def mem_insert(mem:Mem):
    dm = DaoMem()
    cnt = dm.insert(mem.m_id,mem.m_name,mem.tel,mem.email)
    return JSONResponse(content={'cnt':cnt})

@app.post("/mem_update")
async def mem_update(mem:Mem):
    dm = DaoMem()
    cnt = dm.update(mem.m_id,mem.m_name,mem.tel,mem.email)
    return JSONResponse(content={'cnt':cnt})

@app.post("/mem_delete")
async def mem_delete(mem:Mem):
    dm = DaoMem()
    cnt = dm.delete(mem.m_id)
    return JSONResponse(content={'cnt':cnt})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    
    
    