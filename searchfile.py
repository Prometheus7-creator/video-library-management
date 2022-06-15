from screenutil import *
from dbconnection import *

def search_file():
	clear_screen()


	try:
		collection_name = get_database('test', 'vlmdata')

		try:

			items = collection_name.find()

			file_to_search = input('Enter file name: ')
			print()

			found = False

			for item in items:
				if item['filename'] == file_to_search:
					print('File exists')
					print()

					print('Path: ', item['path'])
					print('Filename: ', item['filename'])

					found = True


			if not found:
				print('No file matched')
			

		except:
			print('Search unsuccessful')


	except:

		print('Database connection unsuccessful')

	print()
	print()

	_ = input('Enter any character to go back')

