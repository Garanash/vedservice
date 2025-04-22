from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

router = APIRouter(prefix='/search')


@router.post('/input')
def search_articles(request: Request):
    return templates.TemplateResponse('input_page.html', {'request': request})
