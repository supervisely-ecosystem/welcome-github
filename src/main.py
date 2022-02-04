from fastapi import FastAPI, Request
import names

import supervisely as sly
from supervisely.fastapi_helpers import get_subapp, Jinja2Templates
from supervisely.fastapi_helpers import StateJson, DataJson, LastStateJson, ContextJson

# init state and data (singletons)
LastStateJson({})
DataJson({"name": "<empty>"})

app = FastAPI()
sly_app = get_subapp()
app.mount("/sly", sly_app)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post("/generate")
async def generate(request: Request):
    data = DataJson()
    data["name"] = names.get_first_name()
    await data.synchronize_changes()
