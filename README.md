# Flask-101

Flask setup

pip install flask  
Open any text editor for python and create a file ‘hello_flask.py’  

Write hello world problem
'''python
from flask import Flask
app =Flask(__name__)

@app.route(“/”) 
def run():
return “Hello World”
'''

Set the flask variable to the file name by using
'''
set FLASK_APP=hello_flask.py
'''
This has to be done again if the terminal is closed.  
To run the program  

flask run 
If any changes are made to the program you have to stop the server and run set FLASK_APP=hello_flask.py again.  
So you can use the command  
set FLASK_DEBUG=1  
which now shows the changes made to the python code when the webpage is refreshed.  
Otherwise you can add   
'''python
if __name__ == __main__:
app.run(debug=True)
'''  
And now run directly by using the python command  
python hello_flask.py  

You can add more routes
'''
@app.route("/about")
def about():
    return "<h1>About Page</h1>"
'''

So when you search http://localhost:5000/about you will get ‘About page’ printed
You can add more html functionality but it makes the code ugly if you add html code for each route. 
Code: 
'''
def about():
    return ```<!doctype html>
	<html>
<h1> This is the about page</h1>
</html>
'''

Alternative approach to that is to use templates  
Create home.html and about.html files   

From flask import Flask, render_template  
Code: 
'''python
def about():
return render_template(‘about.html’)
'''

This displays the html code on the server with the python file clean and easy to make any changes in future.  
There might be redundant code in multiple html files which can be minimised by using a single file for the code which is constant in all the html files and inherit from those files.   
With the use of {% block content %}{% endblock content %} in the main file(layout.html)  
And now defining the block in other html files accordingly   
Bootstrap, the world’s most popular framework for building responsive, mobile-first sites.  





