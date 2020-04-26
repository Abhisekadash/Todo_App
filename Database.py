'''This is the database configuration of the TODO App.

It store the items and item status.

'''
import mysql.connector
'''
Using mysql.connector To connect python to database 
by using username password

'''
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="chiku123",
  database="todo_list",auth_plugin='mysql_native_password',
)
# Invoke curser() to access the db.  
mycursor=mydb.cursor()

# insert_items() for insert elements.
def insert_items(item1,status1):
	sql="insert into items(items,status) values (%s,%s)"
	val=(item1,status1)
	mycursor.execute(sql,val)
	mydb.commit()

# To display the item and item status.
def display():
	mycursor.execute("select * from items")
	mylist=mycursor.fetchall()
	return mylist

# To delete the item from database.
def delete_items(id1):
	sql="delete from items where items = %s"
	val=(id1,)
	mycursor.execute(sql,val)
	mydb.commit()

# This will update the item from incomplete to coomplete or vice-versa.
def update_items(item_name,status2):
	sql="update items set status=%s where items=%s"
	val=(status2,item_name)
	mycursor.execute(sql,val)
	mydb.commit()

'''

End of Application

'''