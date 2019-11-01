from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def basic():
    return render_template('index.html')

@app.route('/auth',methods=["POST"])
def auth():
    data = request.form #immutable dictionry
    print(data["uname"])
    return render_template('index2.htm')






@app.route('/about')
def basic2():
    name="chetan"
    return render_template('about.html',name=name)

app.run(debug=True)