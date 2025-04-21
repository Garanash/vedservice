import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

temlates = Jinja2Templates(directory='templates')

application = FastAPI()


@application.get('/')
def start_page(request: Request):
    return temlates.TemplateResponse('start.html', {'request': request})


if __name__ == '__main__':
    uvicorn.run('main:application')
