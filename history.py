from screenutil import *
from dbconnection import *

def show_history():
	clear_screen()


	try:
		collection_name = get_database('test', 'vlmdata')

		try:

			items = collection_name.find()

			index = 1
			for item in items:

				for column in (index, item['path'], item['filename']):
					print(column, end = ' ')

				try:
					print(item['last played'], end = ' ')
				except:
					print('Not played before', end = ' ')

				print()

				index+=1

		except:
			print('Operation unsuccessful')


	except:

		print('Database connection unsuccessful')


	print()
	print()

	_ = input('Enter any character to go back')