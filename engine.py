import json
from pathlib import Path
from models import FileState
from data import Baseline


class Scanner():
    def __init__(self, dir_path):
        self.base_dir = Path(dir_path)
    
    def get_files(self):
        files = {}
        files[str(self.base_dir.resolve())] = {}
        for obj in self.base_dir.rglob("*"):
            if obj.is_file():
                file = FileState(obj)
                files[str(self.base_dir.resolve())][str(obj.resolve())] = file.get_hash()
        return files
    
    def check_baseline(self):
        baseline_path = Path(__file__).parent / "baseline.json"
        if not baseline_path.is_file():
            return False
        with baseline_path.open("r") as f:
            current_baseline = json.load(f)
        if not str(self.base_dir.resolve()) in current_baseline:
            return False
        return True

    def save_scan(self, scan_data):
        baseline_data = Baseline()
        return baseline_data.write_baseline(scan_data)


        