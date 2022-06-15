from login import *
from screenutil import *
from main_menu import*

import getpass


if __name__ == "__main__":

    clear_screen()
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    
    if (login(username, password)):
        # print('logged in')

        main_menu()
    else:
        clear_screen()
        print('invalid access')