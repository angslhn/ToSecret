from os.path import dirname, abspath, join
from sys import exit
from typing import Optional
from types import FrameType
from signal import signal, SIGINT
from libs import banner, menu, option, prompt_password, confirm_hide_extension, process

def handler(_sig: int, _frame: Optional[FrameType]):
    print("\n\n    " + "[x] Exit the program...")
    exit(0)

signal(signalnum=SIGINT, handler=handler)

def main():
    base_path = dirname(abspath(__file__))
    
    output_path = join(base_path, "output")
        
    banner()
    menu()
    selected = option()
    process(base_path=base_path, output_path=output_path, prompt_password=prompt_password, confirm_hide_extension=confirm_hide_extension, option=selected)

if __name__ == "__main__":
    main()