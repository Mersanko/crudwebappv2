from flask import Flask,render_template, redirect, request,url_for,flash
from app import app
import app.studentModel as model1
import app.courseModel as model2
import app.departmentModel as model3 
import app.collegeModel as model4

@app.route('/')
@app.route('/index')
def index():
	data = model1.student.readAll()
	datacounts = 0
	for d in data:
		datacounts+=1

	courses = model1.student.courses()
	departments  = model1.student.departments()
	colleges = model1.student.colleges()
	return render_template('index.html',title="Student List",students=data,courses=courses,departments=departments,colleges=colleges,datacounts=datacounts)

@app.route('/insert', methods=['POST','GET'])
def insert():
	if request.method == 'POST':
		flash(u'Data inserted successfully!','success')
		stdt = model1.student(firstName=request.form['firstName'],lastName=request.form['lastName'],age=request.form['age'],gender=request.form['gender'],contactno=request.form['contactno'],course=request.form['course'],yearLevel=request.form['yearLevel'])
		crs = request.form['course']
		stdt.add(crs)
	return redirect(url_for('index'))
	
@app.route('/update',methods=['POST'])
def update():
	if request.method == 'POST':
		flash(u'Data updated successfully!','warning')
		stdt = model1.student(firstName=request.form['firstName'],lastName=request.form['lastName'],age=request.form['age'],gender=request.form['gender'],contactno=request.form['contactno'],course=request.form['course'],yearLevel=request.form['yearLevel'])
		idno = request.form['idno']
		crs = request.form['course']
		stdt.update(idno,crs)
		return redirect('/')
	else:
		return redirect(url_for('index'))

@app.route('/delete/<int:rawid>')
def delete(rawid):
	stdt = model1.student()
	stdt.delete(rawid)
	flash(u'Data deleted successfully!','success')
	return redirect('/')


@app.route('/courses')
def courses():
	courses = model1.student.courses()
	departments  = model1.student.departments()
	colleges = model1.student.colleges()
	dataCounts = 0
	for c in courses:
		dataCounts+=1
	return render_template('courses.html',title='Course List',colleges=colleges,departments=departments,courses=courses,dataCounts=dataCounts)


@app.route('/departments')
def departments():
	dprtmnts  = model3.department()
	departments = dprtmnts.readAll()
	cllgs = model4.college()
	colleges = cllgs.readAll()
	dataCounts = 0
	for d in departments:
		dataCounts+=1
	return render_template('departments.html',title='Department List',colleges=colleges,departments=departments,dataCounts=dataCounts)



@app.route('/colleges')
def colleges():
	colleges = model4.college()
	data = colleges.readAll()
	dataCounts = 0
	for d in data:
		dataCounts+=1
	return render_template('colleges.html',title='College List',colleges=data,dataCounts=dataCounts)

@app.route('/insertcollege',methods=['POST','GET'])
def insertCollege():
	if request.method == 'POST':
		flash(u'Data added successfully!','success')
		cllg = model4.college(collegeCode=request.form['collegeCode'],collegeName=request.form['collegeName'])
		cllg.add()
	return redirect('/colleges')



@app.route('/deletecollege/<int:collegeNo>')
def deletecollege(collegeNo):
	cllg = model4.college()
	msg = cllg.delete(collegeNo)
	flash(msg[0],msg[1])
	return redirect('/colleges')

@app.route('/updatecollege/<int:collegeNo>',methods=['POST','GET'])
def updatecollege(collegeNo):
	if request.method == 'POST':
		flash(u'Data updated successfully!','warning')
		cllg = model4.college(collegeCode=request.form['collegeCode'],collegeName=request.form['collegeName'])
		cllg.update(collegeNo)
		return redirect('/colleges')
	else:
		return redirect('/colleges')

@app.route('/insertdepartment',methods=['POST','GET'])
def insertdepartment():
	if request.method == 'POST':
		flash(u'Data added successfully!','success')
		dprtmnt = model3.department(departmentName=request.form['departmentName'],college=request.form['college'])
		dprtmnt.add()
	return redirect('/departments')

@app.route('/updatedepartment/<int:departmentNo>',methods=['POST','GET'])
def updatedepartment(departmentNo):
	if request.method == 'POST':
		flash(u'Data updated successfully!','warning')
		dprtmnt = model3.department(departmentName=request.form['departmentName'],college=request.form['college'])
		dprtmnt.update(departmentNo)
		return redirect("/departments")
	else:
		return redirect("/departments")

@app.route('/deletedepartment/<int:departmentNo>')
def deletedepartment(departmentNo):
	dprtmnt = model3.department()
	msg = dprtmnt.delete(departmentNo)
	flash(msg[0],msg[1])
	return redirect('/departments')

@app.route('/insertcourse',methods=['POST','GET'])
def insertcourse():
	if request.method=='POST':
		flash(u'Data added successfully!','success')
		crs = model2.course(courseCode=request.form['courseCode'],courseName=request.form['courseName'])
		dprtmnt = request.form['department']
		crs.add(dprtmnt)
		return redirect('/courses')	
	else:
		return redirect('/courses')	


@app.route('/deletecourse/<int:courseNo>')
def deletecourse(courseNo):
	crs = model2.course()
	msg =crs.delete(courseNo)
	flash(msg[0],msg[1])
	return redirect('/courses')

@app.route('/updatecourse/<int:courseNo>',methods=['POST','GET'])
def updatecourse(courseNo):
	if request.method =='POST':
		flash(u'Data updated successfully!','warning')
		crs = model2.course(courseCode=request.form['courseCode'],courseName=request.form['courseName'])
		crs.update(courseNo)
		return redirect("/courses")
	else:
		return redirect("/courses")

@app.route('/search',methods=['GET','POST'])
def search():
	searchEntry = request.form['searchInput']
	srch =  model1.student()
	result = srch.search(searchEntry)
	datacounts = 0
	for r in result:
		datacounts+=1

	courses = model1.student.courses()
	departments  = model1.student.departments()
	colleges = model1.student.colleges()

	return render_template('index.html',title="Student List",students=result,courses=courses,departments=departments,colleges=colleges,datacounts=datacounts)
