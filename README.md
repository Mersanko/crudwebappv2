### CRUD Web App
This Web app is built using Python Flask, HTML+CSS, jQuery and mySQL database, the instructions below will serves as a guide to run the server. 
> - Download the source code.
> - Activate the virtual environment, open cmd then go to flaskapp directory and use this command "venv\Scripts\activate.bat" 
> - Run the server by typing the command "flask run"
> - Try the web app, Enjoy!
---
#### Dependecies
> - Python virtual env
##### Virtualenv is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip. 
> - Python Flask (with extensions)
##### Flask is a web development micro-framework in Python.
> - Python Flask-MySQLdb
##### Flask-MySQLdb provides MySQL connection for Flask.
> - Python pyyaml
##### yaml is a human-readable data-serialization language. It is commonly used for configuration files and in applications where data is being stored or transmitted in short in it use in the confiuration of the database connection.
---
#### Important Features of this Web App
###             
> - Login experience for admin or the person who can manage the student data.
![signin](https://user-images.githubusercontent.com/60516646/96337249-42762d00-10b8-11eb-9aff-f9f24eaf86a3.png)
![register](https://user-images.githubusercontent.com/60516646/96337312-c9c3a080-10b8-11eb-89b0-b909b7c60de6.png)
#### Note: In order to login you need to create an admin account.
---
> - `Create` `Read` `Update` `Delete` student data.         
![addstudentdata](https://user-images.githubusercontent.com/60516646/96532566-baae3f80-12be-11eb-98a7-7003da361e2e.png)
![updatestudentdata](https://user-images.githubusercontent.com/60516646/96532579-c13cb700-12be-11eb-8402-7bd70f59d065.png)
![deletestudentdata](https://user-images.githubusercontent.com/60516646/96532585-c3067a80-12be-11eb-8ba2-ce1e90f1ba7a.png)
---
#### NOTE: In able to read all the data from the database you can just reload or press the "Home" in the navbar. 
> - Navbar at Home Page
![navbar](https://user-images.githubusercontent.com/60516646/96337690-6edf7880-10bb-11eb-8589-93b2760cb2b8.png)
#### NOTE: I didn't use base or main layout because each page has different style.   
---
