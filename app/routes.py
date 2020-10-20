from flask import Flask,render_template,url_for,request,redirect,flash
from app import app, mysql



@app.route('/home')
def home():
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM students");
	data = cur.fetchall()
	cur.close()
	return render_template('home.html',students=data)


#this path will insert data to the database table 
@app.route('/insert',methods=['POST'])
def insert():
	
	if request.method == "POST":
		flash("Data inserted successfully!")
		firstNameEntry = request.form['firstName']
		lastNameEntry = request.form['lastName']
		ageEntry = request.form['age']
		sexEntry = request.form['sex']
		phoneNumberEntry = request.form['phoneNumber']
		courseEntry = request.form['course']
		yearLevelEntry = request.form['yearLevel']

		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM record")
		data = cur.fetchall()
		schoolIDEntry = ""
		counter = 1
	
		for i in data:
			counter+=1
		if counter>0 and counter<10 :
			schoolIDEntry = "2020-000"+ str(counter)
		elif counter>=10 and counter<100:
			schoolIDEntry = "2020-00"+ str(counter)
		elif counter>=100 and counter<1000:
			schoolIDEntry = "2020-0"+ str(counter)
		else:
			schoolIDEntry = "2020-"+ str(counter)
		val = 1
		cur.execute("INSERT INTO students(schoolID,firstName,lastName,age,sex,phoneNumber,course,yearLevel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(schoolIDEntry,firstNameEntry,lastNameEntry,ageEntry,sexEntry,phoneNumberEntry,courseEntry,yearLevelEntry));
		cur.execute("INSERT INTO record(noOfInsertion) VALUES (%s)",(val,))
		mysql.connection.commit()
		return redirect(url_for('home'))


#update data in the database table
@app.route("/update",methods= ['POST'])
def update():
	if request.method == 'POST':
		rawIDEntry = request.form['rawID']
		firstNameEntry = request.form['firstName']
		lastNameEntry = request.form['lastName']
		ageEntry = request.form['age']
		sexEntry = request.form['sex']
		phoneNumberEntry = request.form['phoneNumber']
		courseEntry = request.form['course']
		yearLevelEntry = request.form['yearLevel']

		cur = mysql.connection.cursor()
		cur.execute("""UPDATE students SET firstName=%s,lastName=%s,age=%s,sex=%s,phoneNumber=%s,course=%s,yearLevel=%s WHERE rawID=%s""",
			(firstNameEntry,lastNameEntry,ageEntry,sexEntry,phoneNumberEntry,courseEntry,yearLevelEntry,rawIDEntry))
		flash("Data updated successfully!")
		mysql.connection.commit()
		return redirect(url_for('home'))


#delete a tuple in the database table
@app.route("/delete/<string:rawID>",methods=['POST','GET'])
def delete(rawID):
	if len(rawID)!=0:
		cur = mysql.connection.cursor()
		cur.execute("DELETE FROM students WHERE rawID=%s",(rawID,))
		mysql.connection.commit()
		cur.close()
		flash("Data deleted successfully!")
	return redirect(url_for('home'))


#search data using keywords
@app.route("/search",methods=['POST','GET'])
def search():
	msg=""
	searchEntry = request.form['search']
	cur = mysql.connection.cursor()
	cur.execute("""SELECT * FROM students WHERE schoolID=%s or firstName=%s or lastName=%s or age=%s or sex=%s or phoneNumber=%s or course=%s or yearLevel=%s""",(searchEntry,searchEntry,searchEntry,searchEntry,searchEntry,searchEntry,searchEntry,searchEntry));
	searchData = cur.fetchall()
	cur.close()
	if len(searchData)==0:
		flash(u"Your search- "+ searchEntry+ " -did not match any data",'error')
	return render_template('home.html',students=searchData)
	
# path for signin
@app.route("/",methods=['POST','GET'])
def signin():
	msg = ""
	if request.method=='POST':
		emailEntry = request.form['email']
		passwordEntry = request.form['password']
		
		cur = mysql.connection.cursor()
		cur.execute("""SELECT * FROM admin""");
		data = cur.fetchall()
		for datum in data:
			if  emailEntry==datum[3] and passwordEntry==datum[4]:
				return redirect(url_for('home'))
		else:
			msg = "Incorrect email or password!"
	return render_template('signin.html',msg=msg)
	
#path for registration 
@app.route("/register",methods=['POST','GET'])
def register():
	msg1 = "" #this message if for success
	msg2 = "" #this message if for error
	if request.method=='POST':
		firstNameEntry = request.form['firstName']
		lastNameEntry = request.form['lastName']
		emailEntry = request.form['email']
		passwordEntry = request.form['password']
		confirmPasswordEntry = request.form['confirmPassword']
		cur = mysql.connection.cursor()
		cur.execute("""SELECT * FROM admin WHERE email LIKE %s""",[emailEntry])
		account = cur.fetchone()

		if passwordEntry!=confirmPasswordEntry:
			msg2="Password doesn't match!"
		elif account:
			msg2="Account Already Exist!"
		else:
			cur.execute("""INSERT INTO admin(firstName,lastName,email,password) VALUES (%s,%s,%s,%s)""",(firstNameEntry,lastNameEntry,emailEntry,passwordEntry));
			mysql.connection.commit()
			msg1="Account added successfully, Login now!"
	return render_template('register.html',msg1=msg1,msg2=msg2)

