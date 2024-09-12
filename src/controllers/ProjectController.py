from .BaseController import BaseController
from models import ResponseSignal
from fastapi import UploadFile
import os

class ProjectController(BaseController):
    def __init__(self) -> None:
        super().__init__()

    def get_project_path(self, project_id: str) -> str:
        # Defining the project path that will be saved in.
        project_dir = os.path.join(
            self.files_dir,
            project_id
        )

        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
        return project_dir

