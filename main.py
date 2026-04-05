import sys
from engine import Scanner
from data import Diff


def main():
    directory = sys.argv[2]
    scan = Scanner(directory)
    found_files = scan.get_files()
    if sys.argv[1] == "-r":
        if scan.check_baseline():
            diff = Diff(directory, found_files)
            old_baseline = diff.get_old_data()
            report = diff.report_diff(old_baseline)
            print(report)
            sys.exit(0)
        else:
            print("No baseline for the informed directory currently exists.")
            sys.exit(1)
    elif sys.argv[1] == "-c":
        if(scan.save_scan(found_files)):
            print("Baseline created.")
            sys.exit(0)
        else:
            print("Error.")
            sys.exit(1)
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("""Usage: python3 main.py <flag> <dir_to_monitor>
        Flags: 
        -r: Print diff report
        -c: Create new baseline (overwrites current one)""")
        sys.exit(1)
    main()
