from fastapi import FastAPI

from routes.health import router as health_router
from routes.reports import router as reports_router
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="LLM Reports Service", version="0.1.0")

# Register routers
app.include_router(health_router)
app.include_router(reports_router)
