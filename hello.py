from flask import Flask

myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return "Hello World"

@myapp.route("/Thiri")
def Thiri():
    return "Hello Thiri Than Shwe"
