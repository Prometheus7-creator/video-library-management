from os import system, name

def clear_screen():
    # for windows
    if name=='nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')