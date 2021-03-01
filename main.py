from flask import Flask,request,jsonify,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enter',methods=["POST","GET"])
def recieve():
    if request.method=="POST":
        req=request.form
        print(req)
        if(req['filter']=="Content Based"):
            print("Inside")
            suggestions="Passed"
            return render_template("home.html",Results="suggestions are {}".format(suggestions))
        else:
            return render_template("home.html")

if __name__=='__main__':
    print("Server Initialized")
    app.run(debug=True)