import sys
from rich import print
from .file_reader import read_file
from .diff_checker import check_differences


def main():
    # Print Usage message if enough arguments are not passed.
    if len(sys.argv) < 3:
        print("Usage:")
        print("\tMust provide two file names as command-line arguments.")
        print("\tdiff.py <original_file> <changed_file>")
        exit(1)

    original = sys.argv[1]
    changed = sys.argv[2]

    # Read the contents of the files in lists.
    original_contents = read_file(original)
    changed_contents = read_file(changed)

    # Check and print differences.
    check_differences(original_contents, changed_contents)
