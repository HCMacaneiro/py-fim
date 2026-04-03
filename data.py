import json
from models import FileState
from pathlib import Path


class Baseline():
    def __init__(self):
        self.path = Path(__file__).parent / "baseline.json"
    
    def write_baseline(self, data):
        try:
            with self.path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)
        except Exception as e:
            print(e)
            return False
        return True 
