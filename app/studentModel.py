from app import app,mysql

class student():
	def __init__(self,firstName=None,lastName=None,age=None,gender=None,contactno=None,course=None,yearLevel=None):
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
		self.gender = gender
		self.contactno = contactno
		self.course = course
		self.yearLevel = yearLevel

	@classmethod
	def readAll(cls):
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM students");
		data = cur.fetchall()
		cur.close()
		return data

	@classmethod
	def courses(cls):
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM course");
		courses = cur.fetchall()
		cur.close()
		return courses

	@classmethod
	def departments(cls):
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM department");
		departments = cur.fetchall()
		cur.close()
		return departments

	@classmethod
	def colleges(cls):
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM college 	");
		colleges = cur.fetchall()
		cur.close()
		return colleges


	def add(self,crs):
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM record")
		data = cur.fetchall()
		idno = ""
		val = 1
		counter = 1
		
		#idno setup 
		for i in data:
			counter+=1
		if counter>0 and counter<10 :
			idno = "2020-000"+ str(counter)
		elif counter>=10 and counter<100:
			idno = "2020-00"+ str(counter)
		elif counter>=100 and counter<1000:
			idno = "2020-0"+ str(counter)
		else:
			idno = "2020-"+ str(counter)
		
		#for department and college setup
	
		cur.execute("SELECT * FROM course WHERE courseNo=%s",(crs,))
		dataForDeptAndCollege = cur.fetchall()
		departmentPK = dataForDeptAndCollege[0][3]
		collegePK = dataForDeptAndCollege[0][4]


		cur.execute("SELECT * FROM department WHERE departmentNo=%s",(departmentPK,))
		dprtmnt = cur.fetchall()
		department = dprtmnt[0][0]

		cur.execute("SELECT * FROM college WHERE collegeNo=%s",(collegePK,))
		cllg = cur.fetchall()
		college = cllg[0][0]
		


		cur.execute("INSERT INTO students(idno,firstName,lastName,age,gender,contactno,course,yearLevel,department,college) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
			(idno,self.firstName,self.lastName,self.age,self.gender,self.contactno,self.course,self.yearLevel,department,college))
		cur.execute("INSERT INTO record VALUES (%s)",(val,))
		mysql.connection.commit()

	def update(self,idno,crs):
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM course WHERE courseNo=%s",(crs,))
		dataForDeptAndCollege = cur.fetchall()
		departmentPK = dataForDeptAndCollege[0][3]
		collegePK = dataForDeptAndCollege[0][4]

		cur.execute("SELECT * FROM department WHERE departmentNo=%s",(departmentPK,))
		dprtmnt = cur.fetchall()
		department = dprtmnt[0][0]

		cur.execute("SELECT * FROM college WHERE collegeNo=%s",(collegePK,))
		cllg = cur.fetchall()
		college = cllg[0][0]


		cur.execute("""UPDATE students SET firstName=%s,lastName=%s,age=%s,gender=%s,contactno=%s,course=%s,yearLevel=%s,department=%s,college=%s WHERE idno=%s""",
			(self.firstName,self.lastName,self.age,self.gender,self.contactno,self.course,self.yearLevel,department,college,idno))
		mysql.connection.commit()

	
	def delete(self,rawid):
		cur = mysql.connection.cursor()
		cur.execute("DELETE FROM students WHERE rawid=%s",(rawid,))
		mysql.connection.commit()
		