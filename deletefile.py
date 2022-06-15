from screenutil import *
from dbconnection import *

def delete_file():
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
			# user choosen index to delete the file

			delete_file_index = int(input('Enter file number: '))-1		# -1 to convert to 0-based index


			query = {'path': meta_data[delete_file_index][1]}

			collection_name.delete_one(query)

			print()

			print('File successfully deleted')

		except:
			print('Deletion unsuccessful')


	except:

		print('Database connection unsuccessful')

