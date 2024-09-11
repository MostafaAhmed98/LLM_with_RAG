from .BaseController import BaseController
from models import ResponseSignal
from fastapi import UploadFile

class DataController(BaseController):
    def __init__(self) -> None:
        super().__init__()
        self.size_scale = 1048576 # the number we will use to conver MB to bytes

    def validate_uploaded_file(self, file: UploadFile):
        # Checking if the current file format is in our allowed formats
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_ALLOWED.value
        
        # Checking if the current file size is equal or lower than our size allowed
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale: # file.size -> bytes, FILE_MAX_SIZE -> MB
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value

        return True, ResponseSignal.FILE_VALIDATED_SUCCESS.value