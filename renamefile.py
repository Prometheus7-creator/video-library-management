from screenutil import *
from dbconnection import *

def rename_file():
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


			query = {'path': meta_data[file_index][1]}

			print()
			# Name to update the file
			new_name = input('Enter new name: ')

			update_query = {'$set': {'filename': new_name}}

			collection_name.update_one(query, update_query)

			print()

			print('File successfully renamed')

		except:
			print('Rename unsuccessful')


	except:

		print('Database connection unsuccessful')

