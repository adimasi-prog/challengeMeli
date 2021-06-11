import mysql.connector

import models.validation
import models.emails

mysql_host = 'mysql'
mysql_database = 'ChallengeMeLi'
mysql_user = 'root'
mysql_pass = '123456'

def get_all_validation_info():
    validations = []
    try:
        connection = get_connection()

        sql_select_Query = """SELECT di.name,
                                    u.email, 
                                    um.user_manager, 
                                    CASE WHEN dic.confidentiality = 'high' OR dic.integrity = 'high' OR dic.availability = 'high'
                                                then 'high'
                                            when dic.confidentiality = 'medium' or dic.integrity = 'medium' or dic.availability = 'medium'
                                                then 'medium'
                                            else 'low'
                                    end as classification
                                from challengemeli.DatabaseInfos as di
                                    inner join challengemeli.DatabaseInfoClassifications as dic
                                    on di.row_id = dic.database_info_id
                                    inner join challengemeli.users as u
                                    on di.owner_id = u.user_id
                                    left join challengemeli.UserManagers as um
                                    on u.user_id = um.user_id"""
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        for row in records:
            validations.append(models.validation.Validation(row[0], row[1], row[2], row[3]))

        cursor.close()

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
    
    return validations

def get_all_email_pending():
    emails = []
    try:
        connection = get_connection()

        command = """ SELECT row_id, `to`, `subject`, body
                        FROM ChallengeMeLi.Emails
                       WHERE sent = 0 """

        cursor = connection.cursor()
        cursor.execute(command)
        records = cursor.fetchall()

        for row in records:
            emails.append(models.emails.Email(row[0], row[1], row[2], row[3], False))

        cursor.close()

    except mysql.connector.Error as error:
        print(f'Failed to insert record into ChallengeMeLi.Emails table {error}')
    finally:
        if connection.is_connected():
            connection.close()
    
    return emails

def get_connection():
    return mysql.connector.connect(host=mysql_host, database=mysql_database, user=mysql_user, password=mysql_pass)