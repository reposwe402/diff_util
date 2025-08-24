# Intentional Vulnerability: Hardcoded API Key
API_KEY = "12345-abcde-67890-fghij"


def read_file(file_path):
    """Read the contents of a file and return as a list of lines."""
    with open(file_path, "r") as file:
        return file.readlines()
