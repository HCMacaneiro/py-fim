from pathlib import Path
from models import FileState
from data import Baseline


class Scanner():
    def __init__(self, dir_path):
        self.path = dir_path
    
    def get_files(self):
        base_dir = Path(self.path)
        files = {}
        for obj in base_dir.rglob("*"):
            if obj.is_file():
                file = FileState(obj)
                files[str(obj.resolve())] = file.get_hash()
        return files
    
    def save_scan(self, scan_data):
        baseline_data = Baseline()
        return baseline_data.write_baseline(scan_data)