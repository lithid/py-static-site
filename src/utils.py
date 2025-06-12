import os
import shutil


def copy_files_recursive(source: str = None, target: str = None, clean: bool = False):
    if not os.path.isdir(source):
        raise Exception("Source is not directory error")

    if clean:
        if os.path.isdir(target):
            shutil.rmtree(target)
            print(f"Cleaned target: ", target)
        os.mkdir(target)
        print("Created target: ", target)

    for file in os.listdir(source):
        source_path = os.path.join(source, file)
        print("\nSource path:", source_path)
        target_path = os.path.join(target, file)
        print("Target path:", target_path, "\n")
        if os.path.exists(source_path):
            if os.path.isdir(source_path):
                print(f"{source_path} exists and is a dir")
                if not os.path.isdir(target_path):
                    os.mkdir(target_path)
                    print("Created target: ", target_path)
                copy_files_recursive(source_path, target_path, False)
            else:
                print(f"{source_path} exists and is a file")
                shutil.copy(source_path, target_path)
                print("Copied: ", source_path, target_path)
