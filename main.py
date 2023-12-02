from fastapi import FastAPI
from Routes.user_routes import router as user_router
from Routes.role_routes import router as role_router
from Routes.search_routes import router as search_router
from Routes.request_routes import router as request_router
from Routes.file_routes import router as file_router

app = FastAPI()
app.include_router(user_router)
app.include_router(role_router)
app.include_router(request_router)
app.include_router(file_router)
app.include_router(search_router)





