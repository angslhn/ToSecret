from os import mkdir, listdir
from os.path import join, exists, isfile, splitext

def find_files(base_path: str) -> list[list[str]]:        
    folder_files_path = join(base_path, "files")
    
    if not exists(folder_files_path):
        mkdir(folder_files_path)
    
    path_name_extension_files: list[list[str]] = []
    
    for file in listdir(folder_files_path):
        file_path = join(folder_files_path, file)
        
        if isfile(file_path):
            name, extension = splitext(file)
            
            path_name_extension_files.append([file_path, name, extension])
            
    return path_name_extension_files