# Clearing the screen
import os
os.system('clear')

import database


#database.create_table()

#database.insert_records()

database.add_one("Tom", "Bishop", "tom@email.com")

database.show_records()