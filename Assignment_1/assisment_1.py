import os

def rename_files(folder_path):
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist or is not a directory.")
        return
    
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    if not files:
        print("The folder is empty. No files to rename.")
        return
    
    files.sort()  
    for index, file in enumerate(files, start=1):
        file_path = os.path.join(folder_path, file)
        file_extension = os.path.splitext(file)[1]
        new_file_name = f"{index}{file_extension}"
        new_file_path = os.path.join(folder_path, new_file_name)
        
        try:
            os.rename(file_path, new_file_path)
            print(f"File '{file}' renamed to '{new_file_name}'")
        except Exception as e:
            print(f"Error renaming file '{file}': {e}")
    
    print("Renaming completed.")


folder = input("Enter the path to the folder: ")
rename_files(folder)
