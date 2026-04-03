import hashlib
from pathlib import Path

class FileState():
    def __init__(self, file):
        self.file = file
    
    def get_hash(self):
        file_content = self.file.read_bytes()
        file_hash = hashlib.sha256()
        file_hash.update(file_content)
        return file_hash.hexdigest()
