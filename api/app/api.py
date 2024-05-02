from fastapi import FastAPI


app = FastAPI()


@app.get("/heathcheck")
async def root():
    return "OK"
