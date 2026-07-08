from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter
from fastapi import Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from atlas.discovery.services import (
    DiscoveryService,
)


router = APIRouter()

templates = Jinja2Templates(
    directory=str(
        Path(__file__).parent / "templates"
    )
)

service = DiscoveryService()


@router.get(
    "/",
    response_class=HTMLResponse,
)
def home(
    request: Request,
) -> HTMLResponse:

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "Atlas Buyer Discovery",
        },
    )


@router.post(
    "/search",
    response_class=HTMLResponse,
)
def search(
    request: Request,
    product: str = Form(...),
    country: str = Form(...),
) -> HTMLResponse:

    buyers = service.discover(
        product=product,
        country=country,
    )

    return templates.TemplateResponse(
        request=request,
        name="results.html",
        context={
            "title": "Search Results",
            "buyers": buyers,
            "product": product,
            "country": country,
            "total": len(buyers),
        },
    )
