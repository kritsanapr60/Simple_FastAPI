from fastapi import FastAPI
from app.routers import book, user, file
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(book.router)
app.include_router(user.router)
app.include_router(file.router)

# Root api / index
@app.get("/")
async def root():
    return {"message": "Hello World, Welcome to my API"}
