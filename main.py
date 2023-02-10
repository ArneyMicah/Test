from fastapi import FastAPI, File, UploadFile
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/files/")
async def create_file(file: bytes = File()):
    print(file)
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    print(file)
    return {"filename": file.filename}
# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8080)
#     print("Server started")