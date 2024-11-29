from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import init_db
from routers.UserRouter import router as user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # İzin verilen originleri belirtin
    allow_credentials=True,
    allow_methods=["*"],  # İzin verilen HTTP metotlarını belirtin
    allow_headers=["*"],  # İzin verilen başlıkları belirtin
)

@app.on_event("startup")
async def startup():
    await init_db()



@app.get('/')
async def get():
    return {'message': 'deneme 3'}

app.include_router(user_router)





