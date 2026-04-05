import sys
from engine import Scanner
from data import Diff


def main():
    directory = sys.argv[1]
    scan = Scanner(directory)
    found_files = scan.get_files()
    if scan.check_baseline():
        diff = Diff(directory, found_files)
        old_baseline = diff.get_old_data()
        report = diff.report_diff(old_baseline)
        print(report)
        sys.exit(1)
    baseline = scan.save_scan(found_files)
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <dir_to_monitor>")
        sys.exit(1)
    main()
