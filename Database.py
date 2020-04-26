'''This is the database configuration of the TODO App.

It store the items and item status.

'''
import psycopg2
'''
Using mysql.connector To connect python to database 
by using username password

'''
def get_connection_and_cursor():
    conn = psycopg2.connect(
        database="df23sq6s0uglsf",
        user = "cbdlrqjcqwyhmp",
        password = "0249dbfc32587f1f9bc9626ebef7d0d665114be41d002f4cc586ed16413fc8a7",
        host = "ec2-34-225-82-212.compute-1.amazonaws.com",
        port = "5432"
     )
    # Invoke curser() to access the db.
    mycursor=conn.cursor()
    return conn, mycursor


# insert_items() for insert elements.
def insert_items(item1,status1):
	conn,mycursor=get_connection_and_cursor()
	sql="insert into items(items,status) values (%s,%s)"
	val=(item1,status1)
	mycursor.execute(sql,val)
	conn.commit()

# To display the item and item status.
def display():
	conn,mycursor=get_connection_and_cursor()
	mycursor.execute("select * from items")
	mylist=mycursor.fetchall()
	return mylist

# To delete the item from database.
def delete_items(id1):
	conn,mycursor=get_connection_and_cursor()
	sql="delete from items where items = %s"
	val=(id1,)
	mycursor.execute(sql,val)
	conn.commit()

# This will update the item from incomplete to coomplete or vice-versa.
def update_items(item_name,status2):
	conn,mycursor=get_connection_and_cursor()
	sql="update items set status=%s where items=%s"
	val=(status2,item_name)
	mycursor.execute(sql,val)
	conn.commit()

'''

End of Application

'''