from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="Templates")


@app.post('/')
def get_data(data: str = Form(...)):
    return f'{data}'

@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('show.html', {'request': request})
   

