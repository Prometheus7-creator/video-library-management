from addfile import *
from deletefile import *
from searchfile import *
from renamefile import *
from playfile import *
from history import *

import time
import sys


def main_menu():
	options = [
			'Add',
			'Delete',
			'Search',
			'Rename',
			'Play',
			'History',
			'exit'
	]

	clear_screen()

	print('**********Main Menu**********')
	print()
	print()

	# Show options
	for i,j in enumerate(options):
		print(i+1,j)


	print()
	print()


	selection = input('Enter choice: ')

	# call function according to choice

	if selection=='1':

		add_file()

	elif selection=='2':
		
		delete_file()


	elif selection=='3':
		
		search_file()

	elif selection=='4':
		
		rename_file()

	elif selection=='5':
		
		play_file()

	elif selection=='6':
		
		show_history()

	else:

		clear_screen()
		sys.exit()

	time.sleep(2)
	# To return to main menu
	main_menu()