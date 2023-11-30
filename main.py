from fastapi import FastAPI
from Routes.user_routes import router as user_router
from Routes.role_routes import router as role_router

app = FastAPI()
app.include_router(user_router)
app.include_router(role_router)








