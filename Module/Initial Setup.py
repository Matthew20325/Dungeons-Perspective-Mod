import os
import shutil

def copy_folder():
    # Define the source folder path
    script_directory = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(script_directory, "Assets", "~mods")

    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return

    # Prompt the user for the target directory
    user_input = input("Enter the path where Dungeons/Content/Paks is located: ")
    target_folder = os.path.join(user_input, "Dungeons", "Content", "Paks")

    # Ensure the target directory exists, create it if not
    try:
        os.makedirs(target_folder, exist_ok=True)
    except Exception as e:
        print(f"Failed to create target directory: {e}")
        return

    # Define the destination for the copied folder
    destination_folder = os.path.join(target_folder, "~mods")

    # Copy the folder
    try:
        if os.path.exists(destination_folder):
            print(f"Destination folder already exists, removing: {destination_folder}")
            shutil.rmtree(destination_folder)

        shutil.copytree(source_folder, destination_folder)
        print(f"Folder copied successfully from {source_folder} to {destination_folder}")
    except Exception as e:
        print(f"Failed to copy folder: {e}")

if __name__ == "__main__":
    copy_folder()
