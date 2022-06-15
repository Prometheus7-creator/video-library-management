from dbconnection import *

def login(user, password):    
    
    # Get the database
    collection_name = get_database('test', 'users')


    item_details = collection_name.find()

    valid = False
    for item in item_details:
        if item['user']==user and item['password']==password:
            valid = True
            break

    if valid:
        
        return True

    return False