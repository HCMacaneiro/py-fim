import sys
from engine import Scanner


def main():
    directory = sys.argv[1]
    scan = Scanner(directory)
    found_files = scan.get_files()
    if scan.check_baseline():
        print("Baseline already exists.")
        sys.exit(1)
    baseline = scan.save_scan(found_files)
    



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <dir_to_monitor>")
        sys.exit(1)
    main()
