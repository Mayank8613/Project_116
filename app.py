# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Mayank" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def home():

    name1 = "Shashank" # write your name
    age1 = "48" # write your age

    return render_template('index.html' , name1 = name1 , age1 = age1)

# define the route to mother webpage
@app.route("/mother")
def home():

    name2 = "Neera" # write your name
    age2 = "47" # write your age

    return render_template('index.html' , name2 = name2 , age2 = age2)

# define the route to brother webpage
@app.route("/friend")
def home():

    name3 = "Mihir" # write your name
    age3 = "21" # write your age

    return render_template('index.html' , name3 = name3 , age3 = age3)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
