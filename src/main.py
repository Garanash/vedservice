import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from api import search_router

templates = Jinja2Templates(directory='templates')

application = FastAPI()
application.include_router(search_router)


@application.get('/')
async def start_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


if __name__ == '__main__':
    uvicorn.run('main:application', reload=True)
