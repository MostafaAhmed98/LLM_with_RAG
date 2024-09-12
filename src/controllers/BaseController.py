from helpers.config import get_settings, Settings
import os

class BaseController():
    def __init__(self) -> None:
        self.app_settings = get_settings()
        self.base_dir = os.path.dirname( os.path.dirname(__file__) ) # -> src  ## getting the parent folder of current file, then getting the parent of the current parent file 
        self.files_dir = os.path.join(self.base_dir, "assets/files") # src/assets/files