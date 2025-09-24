def option() -> int:  
    try:
        return int(input("\n    " + "[=> Selected Menu = "))
    except ValueError:
        return 0
    except EOFError:
        print("\n\n    " + "[x] Exit the program...")
        exit()