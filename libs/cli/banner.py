import textwrap
import shutil

def banner() -> None:
    print("\n   ░▀█▀░█▀█░█▀▀░█▀▀░█▀▀░█▀▄░█▀▀░▀█▀"
          "\n   ░░█░░█░█░▀▀█░█▀▀░█░░░█▀▄░█▀▀░░█░"
          "\n   ░░▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░▀░\n")

    info = {
        "Author": "Aang Solihin",
        "Description": "ToSecret is a program to encrypt and decrypt files.",
        "Version": "1.0"
    }
    
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    
    label_width = max(len(label) for label in info.keys()) + 1
     
    for label, value  in info.items():        
        prefix = f"    {label.ljust(label_width)}: "
        wrapped = textwrap.fill(
            value,
            width=terminal_width,
            initial_indent=prefix,
            subsequent_indent=" " * len(prefix)
        )
        
        print(wrapped)
    
    print()