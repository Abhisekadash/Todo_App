import psycopg2
import os
'''
Using mysql.connector To connect python to database 
by using username password
'''
def get_connection_and_cursor():
	print(os.environ['PORT'])
	print(type(os.environ['PORT']))
	print()
	conn = psycopg2.connect(
        database=os.environ['DATABASE'],
        user = os.environ['USER'],
        password = os.environ['PASSWORD'],
        host = os.environ['HOST'],
        port = 5432,
        )
	mycursor=conn.cursor()
	return conn, mycursor

def create(table):
	conn,mycursor=get_connection_and_cursor()
	table_list=mycursor.execute("show tables")
	if table in table_list:
		print("table present")
	else:
		mycursor.execute("create table items(items varchar(100),status varchar(10))")
	conn.execute()
create(os.environ['TABLE_NAME'])

# insert_items() for insert elements.
def insert_items(item1,status1):
	conn,mycursor=get_connection_and_cursor()
	sql=f"insert into {os.environ['TABLE_NAME']}(items,status) values (%s,%s)"
	val=(item1,status1)
	mycursor.execute(sql,val)
	conn.commit()

# To display the item and item status.
def display():
	conn,mycursor=get_connection_and_cursor()
	mycursor.execute(f"select * from {os.environ['TABLE_NAME']}")
	mylist=mycursor.fetchall()
	return mylist

# To delete the item from database.
def delete_items(id1):
	conn,mycursor=get_connection_and_cursor()
	sql=f"delete from items where {os.environ['TABLE_NAME']} = %s"
	val=(id1,)
	mycursor.execute(sql,val)
	conn.commit()

# This will update the item from incomplete to coomplete or vice-versa.
def update_items(item_name,status2):
	conn,mycursor=get_connection_and_cursor()
	sql=f"update {os.environ['TABLE_NAME']} set status=%s where items=%s"
	val=(status2,item_name)
	mycursor.execute(sql,val)
	conn.commit()

'''

End of Application

'''