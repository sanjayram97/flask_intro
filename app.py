from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',op='')
  
@app.route('/greet',methods = ['POST'])
def analysis():
    name = request.form['nm']
    welcome_text = "Hey "+name+" welcome to Skill Python"
    
    return render_template('index.html',op=welcome_text)
  
if __name__ == '__main__':
   app.run(debug = True)
   
   
   
   