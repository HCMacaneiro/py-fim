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


class Diff():
    def __init__(self, base_dir, new_data):
        self.base_dir = Path(base_dir)
        str_base_dir = str(self.base_dir.resolve())
        self.new_data = new_data.get(str_base_dir, {})

    def get_old_data(self):
        baseline_path = Path(__file__).parent / "baseline.json"
        with baseline_path.open("r") as f:
            current_baseline = json.load(f)
        target_dir = str(self.base_dir.resolve())
        return current_baseline.get(target_dir, {})
    
    def report_diff(self, old_data):
        old_data_keys = set(old_data.keys())
        new_data_keys = set(self.new_data.keys())
        added_files = new_data_keys - old_data_keys
        removed_files = old_data_keys - new_data_keys
        unchanged_files = set()
        changed_files = set()
        for file in new_data_keys.intersection(old_data_keys):
            if self.new_data[file] == old_data[file]:
                unchanged_files.add(file)
            else:
                changed_files.add(file)
        return f"""
        Added: {len(added_files)}
        Removed: {len(removed_files)}
        Changed: {len(changed_files)}

        ---
        Added files: {", ".join(added_files) or None}
        Removed files: {", ".join(removed_files) or None}
        Changed files: {", ".join(changed_files) or None}
        """

