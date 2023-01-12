from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import order_router

app = FastAPI()
app.include_router(order_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    from dotenv import load_dotenv
    import uvicorn
    import sys
    import os

    if sys.platform != 'linux':
        load_dotenv()
        uvicorn.run(app='run:app', host=os.getenv('HOST'), port=int(os.getenv('PORT')), reload=True)
