from fastapi import FastAPI
from core.config import settings
from routers import binance, coingecko
import uvicorn
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Cryptop API", description="API for fetching crypto prices from CoinGecko", version="0.1.0")

logger.info(f"'{settings.PROJECT_NAME}' - Iniciando aplicación...")

# app.include_router(binance.router)
app.include_router(coingecko.router)

logger.info(f"Routers incluidos con prefijo: {settings.API_V1_STR}")

@app.get("/", tags=["Root"])
async def read_root():
    """Endpoint raíz para verificar que la API está activa."""
    return {"message": f"Bienvenido a {settings.PROJECT_NAME}. Visita {settings.API_V1_STR}/docs para la documentación."}

logger.info(f"Aplicación lista. Documentación en http://127.0.0.1:8000{settings.API_V1_STR}/docs")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

