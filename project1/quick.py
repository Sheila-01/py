# from flask import Flask                                    #We imported the Flask Class from the Flask library
from flask import Flask, render_template
from hobbies import count                                    #importing the count method from hobbies
app = Flask(__name__)                                        #Creating an object app from the flask class..... "where the flask app is located"

@app.route("/", methods= ['POST'])                             #The path/root..... server waiting for request
def hello():                                                 #A Function
    return "Hello There, Hope you are doing great"

@app.route("/hello")                                        #Extension in the browser
def Ladies():                                               #The route function
    return render_template('index.html', hobbie="laughing")                    #The return value

@app.route("/greet/<name>")                                 #Extend with /greet/anyname e.g sheila to display
def saluted (name):                                          #Function should have the same naming like in the route i.e "name"
    return f"Goodafternoon {name}"  

@app.route("/greet/<int:number>")                 
def salute (number):                          
    return f"Goodafternoon {number+12}"  

if __name__=="__main__":
    print(__name__)                                                         #prints __main__ as name
    count()
    app.run(debug=True)
