
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import voiture, locataire, location

app = FastAPI()

# Add CORS middleware BEFORE routers for it to work on all routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(voiture.router)
app.include_router(locataire.router)
app.include_router(location.router)