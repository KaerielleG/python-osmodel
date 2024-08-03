import os

def list_directory_contents(path):
    try:
        # List all files and directories in the given path
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(f'Directory: {entry.name}')
                elif entry.is_file():
                    print(f'File: {entry.name}')
    except FileNotFoundError:
        print(f'The directory "{path}" does not exist.')
    except PermissionError:
        print(f'Permission denied to access the directory "{path}".')

if __name__ == "__main__":
    # Prompt the user for the directory path
    directory_path = input("Please enter the directory path: ")
    list_directory_contents(directory_path)
