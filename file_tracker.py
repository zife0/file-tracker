import os
import time

def scan_directory(path):
    files = {}

    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            try:
                files[file_path] = os.path.getmtime(file_path)
            except:
                pass

    return files

def detect_changes(old_state, new_state):
    added = set(new_state) - set(old_state)
    removed = set(old_state) - set(new_state)
    modified = {
        file for file in new_state
        if file in old_state and new_state[file] != old_state[file]
    }

    print("=== File Tracker ===")
    print("Added:", len(added))
    print("Removed:", len(removed))
    print("Modified:", len(modified))

    for file in list(added)[:5]:
        print("+", file)

    for file in list(removed)[:5]:
        print("-", file)

    for file in list(modified)[:5]:
        print("*", file)

def main():
    path = input("Enter directory path: ")

    if not os.path.exists(path):
        print("Directory not found.")
        return

    print("Scanning directory...")
    old_state = scan_directory(path)

    print("Waiting for changes...")
    time.sleep(10)

    new_state = scan_directory(path)
    detect_changes(old_state, new_state)

if __name__ == "__main__":
    main()
