# Hello world program for flask and python.

# Instance of class Flask will be the Web Server Gateway Interface (WSGI)
from flask import Flask

# Create an instance of this class. __name__ is the name of the application's module package.
app = Flask(__name__)

# Use the route() decorator to tell Flask what URL should trigger the function.
@app.route("/<username>")

# Function used to generate URLs for this function, and returns the message to display in the users' browsers.
def hello_world(username):
    return "Hello %s's World!" % username

# If the program is being run by itself, then it will run. If it is imported from another module, it will not.
if __name__ == "__main__":
    print(__name__)
    app.run()
else:
    print(__name__)
    print("I am being imported from another module")

# This can also be run at command line with
# set FLASK_APP=hello.py
# flask run
# or
# python -m flask run
