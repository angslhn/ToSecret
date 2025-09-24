from sys import exit

def confirm_hide_extension() -> str:
    try:
        return input("\n    " + "[=> Hide file extensions (Y/N) = ")
    except EOFError:
        print("\n\n    " + "[x] Exit the program...")
        exit()