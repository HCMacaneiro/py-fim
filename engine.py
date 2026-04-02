from pathlib import Path
from models import FileState


class Scanner():
    def __init__(self, dir_path):
        self.path = dir_path
    
    def hash_files(self):
        base_dir = Path(self.path)
        for obj in base_dir.rglob("*"):
            if obj.is_file():
                file = FileState(obj)
        


if __name__ == "__main__":
    scan = Scanner("/home/hcm/Documents/")
    scan.hash_files()