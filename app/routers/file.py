from fastapi import FastAPI, File, UploadFile, APIRouter
from typing import List

app = FastAPI()

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


router = APIRouter(
    prefix="/img",
    tags=["File"],
    responses={404: {"message": "Not found"}}
)

@router.post("/")
async def up_img(file: UploadFile = File(...)):
    size = await file.read()
    return  { "File Name": file.filename, "size": len(size)}

@router.post("/multi")
async def up_multi_file(files: List[UploadFile] = File(...)):
    file = [
        {
            "File Name":file.filename, 
            "Size":len(await file.read())
        } for file in files]
    return  file