import csv
import persistance.commands
import models.users

user_manager_csv_file_path = '../user_manager.csv'

def import_from_csv_file():
    with open(user_manager_csv_file_path, encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        users = []
        for row in csv_reader:
            user = models.users.UserManager(row[0], row[1], row[2], row[3])
            users.append(user)
        
        return users

def import_and_store_user_managers():
    user_managers = import_from_csv_file()
    for user_manager in user_managers:
        persistance.commands.add_user_manager(user_manager.row_id, user_manager.uid, user_manager.state, user_manager.manager)