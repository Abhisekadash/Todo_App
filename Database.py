import sqlite3
import os
import logging
'''
Using mysql.connector To connect python to database 
by using username password
'''
def get_connection_and_cursor():
	conn=sqlite3.connect('app.db')
	return conn

# insert_items() for insert elements.
def insert_items(item1,status1):
	conn=get_connection_and_cursor()
	sql="insert into todolist(item,status) values (?,?)"
	val=(item1,status1)
	conn.execute(sql,val)
	conn.commit()

# To display the item and item status.
def display():
	conn=get_connection_and_cursor()
	todo_list=conn.execute("select * from todolist")
	mylist=[]
	for x in todo_list:
		mylist.append(list(x))
	return mylist

# To delete the item from database.
def delete_items(id1):
	conn=get_connection_and_cursor()
	sql="delete from todolist where item = ?"
	val=(id1,)
	conn.execute(sql,val)
	conn.commit()

# This will update the item from incomplete to coomplete or vice-versa.
def update_items(item_name,status2):
	conn=get_connection_and_cursor()
	sql="update todolist set status=? where item=?"
	val=(status2,item_name)
	conn.execute(sql,val)
	conn.commit()
'''
End of Application

'''