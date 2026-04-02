import hashlib
from pathlib import Path

class FileState():
    def __init__(self, file):
        self.file = file
    
    def hash_file(self):
        file_content = self.file.read_bytes()
        file_hash = hashlib.sha256()
        file_hash.update(file_content)
        return file_hash 


if __name__ == "__main__":
    test_file = FileState("/home/hcm/Documents/not-an-easter-egg.txt")
    test_file_hash = test_file.hash_file()
    print(test_file_hash.hexdigest())
