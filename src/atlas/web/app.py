from __future__ import annotations

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from atlas.web.routes import router


app = FastAPI(
    title="Atlas",
    version="0.1.0",
)

app.include_router(router)

app.mount(
    "/static",
    StaticFiles(
        directory="src/atlas/web/static",
    ),
    name="static",
)
