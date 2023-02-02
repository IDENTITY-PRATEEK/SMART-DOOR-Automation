import random
import time
import MySQLdb

hostname = '192.168.43.123'
username = 'Internship'
password = '87654321'
database = 'motor'

while True:
    temp = random.randrange(23,50)
    vib = random.randrange(40,95)
    rpm = random.randrange(500,2000)  
    datetime = time.strftime("%Y")+'-' +time.strftime("%m")+'-'+time.strftime("%d")+ " " +time.strftime("%H")+':' +time.strftime("%M")+':'+time.strftime("%S")
   
    insert_stmt = 'INSERT INTO motorcontrol (TimeStamp, RPM, Temperature, Vibration) VALUES (%s,%s,%s,%s)'
    data = [datetime,rpm,temp,vib]
    try:
        conn = MySQLdb.connect(host = hostname, user = username, passwd = password, db = database)
        cursor_obj = conn.cursor()
        cursor_obj.execute(insert_stmt, data)
        conn.commit()
        print(cursor_obj.rowcount,"record inserted")
        
    except Exception as error:
        print(error)

    finally:
        cursor_obj.close()
        conn.close()
        time.sleep(5)