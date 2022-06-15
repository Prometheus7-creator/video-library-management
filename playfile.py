from screenutil import *
from dbconnection import *
import os, sys, subprocess
import time


def play_file():
	clear_screen()


	try:
		collection_name = get_database('test', 'vlmdata')

		try:

			items = collection_name.find()

			meta_data = []

			index = 1
			for item in items:
				meta_data.append((index, item['path'], item['filename']))
				index += 1

				for column in meta_data[-1]:
					print(column, end = ' ')

				print()


			print()
			# user choosen index to the file

			file_index = int(input('Enter file number: '))-1		# -1 to convert to 0-based index

			if sys.platform == 'win32':
				os.startfile(meta_data[file_index][1])
			else:
				opener = "open" if sys.platform == "darwin" else "xdg-open"
				subprocess.call([opener, meta_data[file_index][1]],
					stdout=subprocess.DEVNULL,
					stderr=subprocess.STDOUT
				)

			query = {'path': meta_data[file_index][1]}

			update_last_played = {'$set': {'last played': time.ctime()}}

			collection_name.update_one(query, update_last_played)

		except:
			print('Play file unsuccessful')


	except:

		print('Database connection unsuccessful')

