# app/main.py

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.database import engine, SessionLocal  # Importamos engine para verificar conexión

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Crear instancia de la aplicación FastAPI
# El título aparecerá en la documentación automática (http://localhost:8000/docs)
app = FastAPI(
    title="API de Finanzas Personales",
    description="Backend para gestión de finanzas del hogar",
    version="1.0.0"
)

# Configuración de CORS (Cross-Origin Resource Sharing)
# Esto permite que tu frontend (React) se comunique con el backend
origins = [
    "http://localhost:5173",    # Puerto por defecto de Vite + React
    "http://localhost:3000",    # Por si usas otro puerto
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Orígenes permitidos
    allow_credentials=True,          # Permitir envío de cookies/autenticación
    allow_methods=["*"],             # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],             # Permitir todos los headers
)

# Evento que se ejecuta cuando la aplicación arranca
@app.on_event("startup")
def startup_event():
    """
    Verifica que la conexión a la base de datos sea exitosa al iniciar.
    Si falla, lanza una excepción que detendrá la aplicación.
    """
    try:
        # Intentar conectar a la base de datos
        with engine.connect() as connection:
            print("✅ Conexión a la base de datos establecida correctamente.")
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        # En producción podrías querer relanzar la excepción para que la app no siga
        raise e

# Evento que se ejecuta cuando la aplicación se detiene (opcional)
@app.on_event("shutdown")
def shutdown_event():
    print("🛑 Servidor detenido.")

# Ruta de prueba básica
@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Finanzas Personales"}

# Ruta de prueba para verificar que el entorno funciona
@app.get("/health")
def health_check():
    return {"status": "ok", "environment": os.getenv("ENVIRONMENT", "development")}

# Aquí más adelante incluirás los routers (por ejemplo:)
# from app.api.endpoints import usuarios, transacciones
# app.include_router(usuarios.router, prefix="/api/v1/usuarios", tags=["Usuarios"])
# app.include_router(transacciones.router, prefix="/api/v1/transacciones", tags=["Transacciones"])