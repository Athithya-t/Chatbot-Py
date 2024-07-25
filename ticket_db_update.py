import mysql.connector
mydb=mysql.connector.connect(
    host="AZURE_MYSQL_HOST",
    user="AZURE_MYSQL_USER",
    password="AZURE_MYSQL_PASSWORD",
    database="it-service-chatbot-database")

def create_ticket(id_val,issue,username):
    conn=mydb
    cursor=conn.cursor()
    cursor.execute("insert into tickets (id,issue,username) values (%s,%s,%s)",(id_val,issue,username))
    conn.commit()
    conn.close()


