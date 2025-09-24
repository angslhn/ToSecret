from .encrypt import encrypt
from .decrypt import decrypt
from .init_path import init_path
from typing import Callable

def process(base_path: str, output_path: str, prompt_password: Callable[[], str], confirm_hide_extension: Callable[[], str], option: int) -> None:    
    if option == 1:
        init_path(base_path)
    elif option == 2:
        encrypt(base_path, output_path, prompt_password, confirm_hide_extension)
    elif option == 3:
        decrypt(base_path, output_path, prompt_password)
    elif option == 4:
        print("\n    " + "[x] Exit the menu program...")
        exit()
    else:
        print("\n    " + "[-] No menu options available...")