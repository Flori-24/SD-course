import mysql.connector

#parameters to get connected to db
db_connection = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "Development2426.."
)



db_connection = mysql.connector.connect(
    host = "localhost"
    user= "root"
    password = "Development2426.."
)
cursor= db_connection.cursor()
create_table_query = """

"""

cursor.execute(create_table_query)
print("Table")