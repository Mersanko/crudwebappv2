from app import app,mysql

class college():
	def __init__(self,collegeCode=None,collegeName=None):
		self.collegeCode = collegeCode
		self.collegeName = collegeName
	
	@classmethod
	def readAll(cls):
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM college");
		data = cur.fetchall()
		cur.close()
		return data

	def add(self):
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO college(collegeCode,collegeName) VALUES (%s,%s)",(self.collegeCode,self.collegeName))
		mysql.connection.commit()

	
	def delete(self,cn):
		msg = ""
		cur= mysql.connection.cursor()

		cur.execute("SELECT * FROM students WHERE college=%s",(cn,))
		data1 = cur.fetchone()

		cur.execute("SELECT *  FROM course WHERE college=%s",(cn,))
		data2 = cur.fetchone()

		cur.execute("SELECT * FROM department WHERE college=%s",(cn,))
		data3 = cur.fetchone()

		if data1 is not None or data2 is not None or data3 is not None:
			msg = "Invalid action!, you can only delete a college that does not handle a department, course and with no enrollee/s"
			msgtype = "danger"
			msgtup = (msg,msgtype)
			return msgtup
		else:
			cur.execute("SELECT * FROM college WHERE collegeNo=%s",(cn,))
			data = cur.fetchone()
			msg = "{} has been deleted successfully".format(data[2])
			msgtype = "success"
			msgtup = (msg,msgtype)
			cur.execute("DELETE FROM college WHERE collegeNo=%s",(cn,))
			mysql.connection.commit()
			return msgtup

	
	def update(self,cn):
		cur = mysql.connection.cursor()
		cur.execute("""UPDATE college SET collegeCode=%s,collegeName=%s WHERE collegeNo=%s""",(self.collegeCode,self.collegeName,cn))
		mysql.connection.commit()

	def search(self,searchInput):
		cur= mysql.connection.cursor()
		cur.execute("SET @search=%s",(searchInput,))

		cur.execute("SELECT * FROM college WHERE collegeNo LIKE CONCAT('%',@search,'%') or collegeCode LIKE CONCAT('%',@search,'%') or collegeName LIKE CONCAT('%',@search,'%')")

		data = cur.fetchall()

		return data		

