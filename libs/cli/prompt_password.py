from sys import exit

def prompt_password() -> str:
    try:
        return input("\n    " + "[=> Enter Encryption Password  = ")
    except EOFError:
        print("\n\n    " + "[x] Exit the program...")
        exit()