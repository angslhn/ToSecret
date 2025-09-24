from os import mkdir
from os.path import join, exists
from cryptography.fernet import Fernet
from typing import Callable
from .derive_key import derive_key
from .find_files import find_files

def decrypt(base_path: str, output_path: str, prompt_password: Callable[[], str]) -> None:    
    files = find_files(base_path)
    
    files_failed_to_process: list[str] = []
    
    if len(files) == 0:
        print("\n    " + "[-] There are no files to decrypt...")
        return
    
    print("\n    " + f"[FILES FOUND]:")
    
    for _path, name, extension in files:
        print("    " + f" - {name}{extension}")
        
    print("\n    " + f"[NOTE]:\n{"    "} - Decryption password is the same as encryption password")
    
    bytes_password = prompt_password().encode('utf-8')
    
    failed_process = False
    
    if not exists(output_path):
        mkdir(output_path)
    
    for path, name, extension in files:
        with open(path, mode='rb') as binary:
            file_content = binary.read()
        
        salt = file_content[:16]
        ciphertext = file_content[16:]
        
        key = derive_key(salt, bytes_password)
        
        fernet = Fernet(key)
        
        try:
            data_decrypted = fernet.decrypt(ciphertext)
        except Exception:
            failed_process = True
            
            files_failed_to_process.append(name)
            continue
        
        path_file = (join(output_path, name) + extension)
        
        with open(path_file, mode='wb') as file:
            file.write(data_decrypted)
    
    if failed_process:
        print("\n    " + "[SOME FILE FAILED TO PROCESS]:")
        
        for file in files_failed_to_process:
            print("    " + f" - {file}")
        print("\n    " + "[-] The password does not match or the file contents have changed...")
    else:
        print("\n    " + "[+] Files successfully decrypted...")