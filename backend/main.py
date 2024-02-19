import logging

import uvicorn
from backend import config
from backend.api.api_v1.routers import api_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

API_V1_STR = "/api/v1"
logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="OMMA-Tool API",
    openapi_url=f"{API_V1_STR}/openapi.json",
    docs_url=None
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add the Session Middleware
app.add_middleware(
    SessionMiddleware, secret_key=config.SECRET_KEY, max_age=3600  # 1 hour
)

# include routers
app.include_router(api_router, prefix=API_V1_STR)

# serve static files from the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# custom favicon
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html() -> HTMLResponse:
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_favicon_url="/static/favicon.ico"
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
