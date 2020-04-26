''' This is the server of the Appliccation.

This written in python.

'''
#import flask to connect server side with client side.
from flask import Flask, render_template,redirect,request,url_for

#import database to use the database with python.
import Database

#
app=Flask(__name__)

#app.route('/') is to start the main client side html.
@app.route('/')
def main():
	return render_template('main.html')

#app.route('/index') to start the index.html
@app.route('/index')
def index():
	todo=Database.display()
	return render_template('index.html',todos=todo)

#app.route('/frame') to start the frame.html
@app.route('/frame')
def frame():
	return render_template('frame1.html')
# Finished the UI part

'''       STARTING OF THE FUNCTION PART         '''

# This app.route("/add",methods=['POST']) retrive the items from client  side UI.
@app.route("/add",methods=['POST'])
def  add():

	# Request item through request.form from index.html .
	new_items=request.form['todoitems']
	# To check if the item length is < 32. 
	if len(new_items)<32:
		# To check if the item is alphanumerical.
		if new_items.isalnum():
			# Insert items.
			Database.insert_items(new_items,'Incomplete')
			# This redirect() will execute the index.html  to show the same page. 
			return redirect('/index')
		return redirect('/index')
	else:
		# If item length is >32 then insert only 32 letters.
		Database.insert_items(new_items[0:32],'Incomplete')
		return redirect('/index')

# This will delete the item if someone press delete.
@app.route("/delete1/<id>")
def delete1(id):
	# Delete the item from database
	Database.delete_items(id)
	return redirect('/index')

# This is going to change the Incomplete to Complete or vice-versa.
@app.route("/update/<item>/<status>")
def update(item,status):
	# To change status first check if status is Complete or Incomplete.
	if status=='Incomplete':
		status="Complete"
		# Update the status in database.
		Database.update_items(item,status)
		return redirect('/index')
	else:
		status="Incomplete"
		# Update the status in database.
		Database.update_items(item,status)
		return redirect('/index')

'''

Application will start if __name__=='__main__'

'''
if __name__=='__main__':
	#run() will run the application
	app.run(debug=True)

'''
End of applications.

'''
