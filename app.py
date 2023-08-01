from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Flask"

@app.route('cal', methods=["GET"])
def math_operation():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]
    
    if operation=='add':
        int(number1) + int(number2)
        result = int(number1) + int(number2)
    elif operation =='multiply':
        result = int(number1) * int(number2)
    elif operation =='division':
        result = int(number1) / int(number2)
    else:
        result = int(number1) - int(number2)
        
    

print(__name__)

if __name__=='__main__':
    app.run()