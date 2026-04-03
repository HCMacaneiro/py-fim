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


if __name__ == "__main__":
    file = Path("/home/hcm/Documents/not-an-easter-egg.txt")
    test_file = FileState(file)
    test_file_hash = test_file.get_hash()
    print(test_file_hash)
