from flask import Flask,request,render_template,jsonify
import json

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Flask"

@app.route('/cal', methods=["GET"])
def math_operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]
    
    if operation=='Addition':
        result = int(number1) + int(number2)
    elif operation =='Multiplication':
        result = int(number1) * int(number2)
    elif operation =='Division':
        result = int(number1) / int(number2)
    else:
        result = int(number1) - int(number2)
    return "The Operation is {} and the Result is {}".format(operation,result) 



    

print(__name__)

if __name__=='__main__':
    app.run()