import mysql.connector

mysql_host = 'mysql'
mysql_database = 'ChallengeMeLi'
mysql_user = 'root'
mysql_pass = '123456'
schema_create_script_file_path = './scripts/challenge_meli_schema.txt'

def add_database_info(name, owner_id, time_stamp):
    id = -1
    try:
        connection = get_connection()

        mySql_insert_query = """INSERT INTO ChallengeMeLi.DatabaseInfos (name, owner_id, time_stamp) 
                            VALUES (%s, %s, %s) """

        record_to_insert = (name, owner_id, time_stamp)

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, record_to_insert)
        connection.commit()

        id = cursor.lastrowid
        
        cursor.close()

    except mysql.connector.Error as error:
        print(f'Failed to insert record into ChallengeMeLi.DatabaseInfos table {error}')

    finally:
        if connection.is_connected():
            connection.close()

    return id

def add_database_info_classification(database_info_id, confidentiality, integrity, availability):
    id = -1
    try:
        connection = get_connection()

        mySql_insert_query = """INSERT INTO ChallengeMeLi.DatabaseInfoClassifications (confidentiality, integrity, availability, database_info_id) 
                            VALUES (%s, %s, %s, %s) """

        record_to_insert = (confidentiality, integrity, availability, database_info_id)

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, record_to_insert)
        connection.commit()

        id = cursor.lastrowid
        
        cursor.close()

    except mysql.connector.Error as error:
        print(f'Failed to insert record into ChallengeMeLi.DatabaseInfoClassifications table {error}')

    finally:
        if connection.is_connected():
            connection.close()

    return id

def add_user(user_id, name, email):
    try:
        connection = get_connection()

        mySql_insert_query = """INSERT INTO ChallengeMeLi.Users (user_id, name, email) 
                            VALUES (%s, %s, %s) """

        record_to_insert = (user_id, name, email)

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, record_to_insert)
        connection.commit()

        cursor.close()

    except mysql.connector.Error as error:
        print(f'Failed to insert record into ChallengeMeLi.Users table {error}')

    finally:
        if connection.is_connected():
            connection.close()

def add_validation(db_name, owner_email, manager_email, classification):
    try:
        connection = get_connection()

        command = """ INSERT INTO ChallengeMeLi.Validations (db_name, owner_email, manager_email, classification) 
                            VALUES (%s, %s, %s, %s) """

        record = (db_name, owner_email, manager_email, classification)

        cursor = connection.cursor()
        cursor.execute(command, record)
        connection.commit()
        cursor.close()

    except mysql.connector.Error as error:
        print(f'Failed to insert record into ChallengeMeLi.Validations table {error}')

    finally:
        if connection.is_connected():
            connection.close()

def add_user_manager(row_id, user_id, user_state, user_manager):
    id = -1
    try:
        connection = get_connection()

        mySql_insert_query = """INSERT INTO ChallengeMeLi.UserManagers (row_id, user_id, user_state, user_manager) 
                            VALUES (%s, %s, %s, %s) """

        record_to_insert = (row_id, user_id, user_state, user_manager)

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, record_to_insert)
        connection.commit()

        id = cursor.lastrowid

        cursor.close()

    except mysql.connector.Error as error:
        print(f'Failed to insert record into ChallengeMeLi.UserManagers table {error}')

    finally:
        if connection.is_connected():
            connection.close()

    return id

def add_pending_email(to, subject, body):
    try:
        connection = connection = get_connection()

        command = """ INSERT INTO ChallengeMeLi.Emails (`to`, `subject`, body) 
                            VALUES (%s, %s, %s) """

        record = (to, subject, body)

        cursor = connection.cursor()
        cursor.execute(command, record)
        connection.commit()
        cursor.close()

    except mysql.connector.Error as error:
        print(f'Failed to insert record into ChallengeMeLi.Emails table {error}')

    finally:
        if connection.is_connected():
            connection.close()

def set_email_to_sent(id):
    try:
        connection = connection = get_connection()

        command = f""" UPDATE ChallengeMeLi.Emails 
                            SET sent = 1,
                                sent_at = Now()
                        WHERE row_id = {id} """

        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
        cursor.close()

    except mysql.connector.Error as error:
        print(f'Failed to update record into ChallengeMeLi.Emails table {error}')

    finally:
        if connection.is_connected():
            connection.close()

def create_schema():
    script = read_script()
    try:
        connection = get_connection()

        cursor = connection.cursor()
        
        cursor.execute(""" DROP DATABASE IF EXISTS ChallengeMeLi """)

        cursor.execute(script)

        cursor.close()

    except mysql.connector.Error as error:
        print(f'Failed to create schema {error}')

    finally:
        if connection.is_connected():
            connection.close()

def read_script():
    with open(schema_create_script_file_path) as file:
        return file.read()

def get_connection():
    return mysql.connector.connect(host=mysql_host, database=mysql_database, user=mysql_user, password=mysql_pass)