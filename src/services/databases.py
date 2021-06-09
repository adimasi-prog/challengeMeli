import json
import persistance.commands
import models.databases

database_json_file_path = '../dblist.json'

def import_and_store_databases():
    database_infos = import_from_json_file()
    for database_info in database_infos:
        persistance.commands.add_user(database_info.owner.uid, database_info.owner.name, database_info.owner.email)
        database_info_id = persistance.commands.add_database_info(database_info.name, database_info.owner.uid, database_info.time_stamp)
        persistance.commands.add_database_info_classification(database_info_id, database_info.classification.confidentiality, database_info.classification.integrity, database_info.classification.availability)

def import_from_json_file():
    with open(database_json_file_path) as json_file:
        data = json.load(json_file)
        databases = []
        if 'db_list' in data:
            for db in data['db_list']:
                classification = get_database_classification(db)
                owner = get_database_owner(db)
                database = get_database(db, classification, owner, db['time_stamp'])
                databases.append(database)

        return databases

def get_database_classification(json):
    classification = models.databases.DatabaseClassification('empty', 'empty', 'empty')
    if 'classification' in json:
        json_classification = json['classification']
        if 'confidentiality' in json_classification:
            classification.confidentiality = json_classification['confidentiality']

        if 'integrity' in json_classification:
            classification.integrity = json_classification['integrity']

        if 'availability' in json_classification:
            classification.availability = json_classification['availability']
    
    return classification

def get_database_owner(json):
    owner = models.databases.DatabaseOwner('empty', 'empty', 'empty')
    if 'owner' in json:
        json_owner = json['owner']
        if 'name' in json_owner:
            owner.name = json_owner['name']

        if 'uid' in json_owner:
            owner.uid = json_owner['uid']

        if 'email' in json_owner:
            owner.email = json_owner['email']
    
    return owner

def get_database(json, classification, owner, time_stamp):
    database = models.databases.DatabaseInfo('empty', classification, owner, time_stamp)
    if 'dn_name' in json:
        database.name = json['dn_name']

    return database