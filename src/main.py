from http import HTTPStatus

from fastapi import FastAPI

from src.api.v_0_1.routers.cats import router as cats_router
from src.api.v_0_1.routers.helper import router as helper_router

app = FastAPI(
    title="Cats Service",
    version="0.1",
)
app.include_router(helper_router)
app.include_router(cats_router)


@app.get(path="/ping", summary="Ping api", tags=["Ping"], status_code=HTTPStatus.OK)
def ping():
    return f"{app.title}. Version {app.version}"
