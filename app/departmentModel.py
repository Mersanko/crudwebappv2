from app import app,mysql


class department():
	def __init__(self,departmentName=None,college=None):
		self.departmentName = departmentName
		self.college = college
	
	@classmethod
	def readAll(cls):
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM department")
		departments = cur.fetchall()
		cur.close()
		return departments

	def add(self):
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO department(departmentName,college) VALUES (%s,%s)",(self.departmentName,self.college))
		mysql.connection.commit()

	def update(self,dn):
		cur = mysql.connection.cursor()
		cur.execute("""UPDATE department SET departmentName=%s,college=%s WHERE departmentNo=%s""",(self.departmentName,self.college,dn))
		mysql.connection.commit()

	def delete(self,dn):
		msg = ""
		cur = mysql.connection.cursor()

		cur.execute("SELECT * FROM students WHERE department=%s",(dn,))
		data1 = cur.fetchall()

		cur.execute("SELECT * FROM course WHERE department=%s",(dn,))
		data2 = cur.fetchall()
		if len(data1)!=0 or len(data2)!=0:
			msg="Invalid action!, you can only delete a department that does not handle a course and students"
			msgtype = "danger"
			msgtup = (msg,msgtype)
			return  msgtup
		else:
			cur.execute("SELECT * FROM department WHERE departmentNo=%s",(dn,))
			data = cur.fetchone()
			msg="{} has been deleted successfully!".format(data[1])
			msgtype = "success"
			cur.execute("DELETE FROM department WHERE departmentNo=%s",(dn,))
			mysql.connection.commit()
			msgtup = (msg,msgtype)
			return msgtup