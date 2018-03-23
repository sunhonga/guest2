# coding=utf-8
import pymysql.cursors

# Connect to the database

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='123456',
                             db='guest',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor :
        # Create a new record
        sql = 'INSERT INTO sign_guest (realname,phone,email,sign,event_id,create_time) VALUES ("alen",18800110001,"alen@mail.com",0,1,NOW());'
        cursor.execute(sql)

        #connect is not autocommit by default. So you must commit to save
        #your change.
        connection.commit()

    with connection.cursor() as cursor:
        #Read a single record
        sql = "SELECT realname,phone,email,sign FROM sign_guest WHERE phone=%s"
        cursor.execute(sql,('18800110001',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()










