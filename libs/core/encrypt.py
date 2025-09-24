from os import urandom, mkdir
from os.path import join, exists
from cryptography.fernet import Fernet
from typing import Callable
from .find_files import find_files
from .derive_key import derive_key

def encrypt(base_path: str, output_path: str, prompt_password: Callable[[], str], confirm_hide_extension: Callable[[], str]):
    files = find_files(base_path=base_path)
    
    if len(files) == 0:
        print("\n    " + "[-] There are no files to encrypt...")
        return
    
    print("\n    " + f"[FILES FOUND]:")
    
    for _path, name, extension in files:
        print("    " + f" - {name}{extension}")
    
    print("\n    " + f"[NOTE]:\n{"    "} - Don't forget the encryption password\n{"    "} - Don't change the contents of the encrypted file")
    
    hide_extension = False
        
    bytes_password = prompt_password().encode("utf-8")
    
    to_hide_extension: str = confirm_hide_extension()
    
    if to_hide_extension == "Y":
        hide_extension = True
    elif to_hide_extension == "N":
        hide_extension = False
    else:
        print("\n    " + "[-] Invalid choice...")
        return
    
    if not exists(output_path):
        mkdir(output_path)
    
    for path, name, extension in files:
        salt = urandom(16)
        
        key = derive_key(salt, bytes_password)
    
        fernet = Fernet(key)
        
        with open(path, mode='rb') as binary:
            file_content = binary.read()
        ciphertext = fernet.encrypt(file_content)
        
        file_save_path = join(output_path, name) if hide_extension == True else (join(output_path, name) + extension)
        
        with open(file_save_path, mode='wb') as file:
            file.write(salt + ciphertext)
    
    print("\n    " + "[+] Files successfully encrypted...")