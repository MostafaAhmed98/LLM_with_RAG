from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
from models import ResponseSignal
import os
import aiofiles

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=['api_v1', 'data']
)

@data_router.post("/upload/{project_id}")
async def upload_file(project_id: str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
    
    # Making Sure that our project(file) format is valid
    is_valid, signal_message = DataController().validate_uploaded_file(file=file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal_message": signal_message
            }
        )
    
    # Getting the project and file path to save it.
    project_dir_path = ProjectController().get_project_path(project_id=project_id) # src/assets/files/{project_id}
    file_path = os.path.join(project_dir_path,file.filename) # # src/assets/files/{project_id}/{file_name}

    # Split the file to chunks, then save them (More Meomery Efficecient Way)
    async with aiofiles.open(file_path, 'wb') as f:
        while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
            await f.write(chunk)

    return JSONResponse(
        content={
            "Message_Signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value
        }
    )
    


