from screenutil import *
from dbconnection import *

def add_file():
	clear_screen()


	try:
		collection_name = get_database('test', 'vlmdata')

		try:

			num_files = int(input('Number of files: '))


			# store multiple documents
			documents = []

			for i in range(num_files):
				clear_screen()
				path = input('file path: ')
				print()
				filename = input('filename: ')

				item = {
					'path': path,
					'filename': filename
				}

				documents.append(item)

			collection_name.insert_many(documents)

			print()

			print('Files successfully added')

		except:
			print('Insertion unsuccessful')


	except:

		print('Database connection unsuccessful')

