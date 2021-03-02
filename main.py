from flask import Flask,request,jsonify,render_template
import model
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
            try:
                obj=model.get_rec(req['movie'])
                strings=[]
                for i,j in obj.items():
                    strings.append(j)
                return render_template("home.html",movie=req['movie'],r=strings,ask="success")
            except:
                index=model.get_similar_movie(req['movie'])
                obj=model.get_rec(index[0])
                strings=[]
                for i,j in obj.items():
                    strings.append(j)
                return render_template("home.html",movie=index[0],r=strings,ask="success")
        if(req['filter']=='Collaborative Based'):
            return render_template("home.html",ask="colab")

        else:
            return render_template("home.html")

if __name__=='__main__':
    print("Server Initialized")
    app.run(debug=True)