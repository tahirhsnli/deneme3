from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from database import init_db
from routers.UserRouter import router as user_router

app = FastAPI()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Railway PORT dəyişəni və ya 8000 default
    app.run(app, host="0.0.0.0", port=port)

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





