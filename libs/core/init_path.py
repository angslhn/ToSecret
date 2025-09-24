from os import mkdir
from os.path import join, exists

def init_path(base_path: str) -> None:
    path_files = join(base_path, "files")
    path_output = join(base_path, "output")
    
    if not exists(path_files):
        mkdir(path_files)

    if not exists(path_output):
        mkdir(path_output)
        
    print("\n    " + "[+] Folder created successfully...")
    