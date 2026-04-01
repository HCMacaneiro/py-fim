import sys
from models.py import FileState


def main():
    directory = sys.argv[1]
    



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <dir_to_monitor>")
        sys.exit(1)
    main()
