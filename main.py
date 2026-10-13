from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import auth, scholarships, applications

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Scholarship Management API",
    description="A system to manage scholarships and student applications",
    version="1.0.0",
)

# CORS middleware for frontend (supports localhost, Vercel, and custom domains)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_origin_regex=r".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(auth.router)
app.include_router(scholarships.router)
app.include_router(applications.router)


@app.get("/")
def root():
    return {"message": "Scholarship Management API", "version": "1.0.0"}
