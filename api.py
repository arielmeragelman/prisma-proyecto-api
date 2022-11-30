from fastapi import FastAPI, UploadFile
import os
app = FastAPI()


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    '''create_upload_file: a file is uploaded and saved to the relative folder directory.

    Args:
        file (UploadFile): uploaded file to save.

    Returns:
        log: success or fail as a logger response.
    '''

    folder = './data'
    # Create folder if it doesn't exist.
    if not os.path.isdir(folder):
        os.mkdir(folder)

    file_location = f"{folder}/{file.filename}" # Guardar a la carpeta 'data'.
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}