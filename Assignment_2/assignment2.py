import os
import zipfile

def zip_folder(folder_path):
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist or is not a directory.")
        return
    
    zip_file_name = os.path.basename(folder_path.rstrip(os.sep)) + ".zip"
    zip_file_path = os.path.join(os.path.dirname(folder_path), zip_file_name)
    
    try:
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname)
        print(f"Folder successfully zipped into: {zip_file_path}")
    except Exception as e:
        print(f"Error during zipping: {e}")


folder = input("Enter the path to the folder: ")
zip_folder(folder)
