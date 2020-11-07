from app import app,mysql

class course():
	def __init__(self,courseCode=None,courseName=None,department=None,college=None):
		self.courseCode = courseCode
		self.courseName = courseName
		self.department = department
		self.college = college

	@classmethod
	def readAll(cls):
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM course")
		data = cur.fetchall()

	def add(self,dprtmnt):
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM department WHERE departmentNo=%s",(dprtmnt,))
		department = cur.fetchall()
		cur.execute("INSERT INTO course(courseCode,courseName,department,college) VALUES (%s,%s,%s,%s)",(self.courseCode,self.courseName,department[0][0],department[0][2]))
		mysql.connection.commit()

	def delete(self,crs):
		msg = ""
		cur = mysql.connection.cursor()

		cur.execute("SELECT * FROM students WHERE course=%s",(crs,))
		data = cur.fetchall()
		if len(data)!=0:
			msg = "Invalid action!, you can only delete a course with no enrollees"
			msgtype = "danger"
			msgtup = (msg,msgtype)
			return msgtup
		else:
			cur.execute("SELECT * FROM course WHERE courseNo=%s",(crs,))
			data = cur.fetchone()
			msg  = "{} deleted successfully".format(data[2])
			msgtype = "success"
			msgtup = (msg,msgtype)
			cur.execute("DELETE FROM course WHERE courseNo=%s",(crs,))
			mysql.connection.commit()
			return msgtup

	def update(self,crs):
		cur = mysql.connection.cursor()
		cur.execute("UPDATE course SET courseCode=%s, courseName=%s WHERE courseNo=%s",(self.courseCode,self.courseName,crs))
		mysql.connection.commit()

