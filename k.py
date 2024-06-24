import os

def extract_file_names(folder_path):
    file_names = []
    # Check if the folder exists
    if os.path.exists(folder_path):
        # Iterate through all files in the folder
        for file_name in os.listdir(folder_path):
            # Check if the path is a file (not a directory)
            if os.path.isfile(os.path.join(folder_path, file_name)):
                file_names.append(file_name)
    else:
        print("Folder not found.")
    return file_names

# Example usage:
folder_path = "/home/vybog/Jaya_FEb 5/April/Apr-2_json/ja,"
file_names = extract_file_names(folder_path)
print("File names in the folder:")
for name in file_names:
    print(name)
