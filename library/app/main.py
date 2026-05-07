from fastapi import FastAPI
from app.database import engine, Base
from app.routers import books, authors

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Library Management System",
    description="A modern FastAPI framework for managing a library's books, authors, and members.",
    version="1.0.0",
)

# Include routers
app.include_router(books.router)
app.include_router(authors.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Library Management System API",
        "docs": "/docs"
    }
