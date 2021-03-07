from flask import Flask,request,jsonify,render_template
import model
from sqlalchemy import create_engine
engine = create_engine("postgres://ikmjthcnmtxame:08fdd878f97d221cf8b1d42d43d7ac175ced90898127b17a56c4a6dc5373e96b@ec2-54-90-13-87.compute-1.amazonaws.com:5432/dfqcdcdi9h7oi1")
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
                query=req['movie']
                print(query)
                obj=engine.execute("SELECT * FROM movies_2 WHERE Index='{0}'".format(query)).fetchall()
                strings=[]
                for j in obj[0][1:]:
                    strings.append(j)
                return render_template("home.html",movie=req['movie'],r=strings,ask="success")
            except:
                index=model.get_similar_movie(req['movie'])
                query=index[0]
                obj=engine.execute("SELECT * FROM movies_2 WHERE Index='{0}'".format(query)).fetchall()
                strings=[]
                for j in obj[0]:
                    strings.append(j)
                return render_template("home.html",movie=index[0],r=strings,ask="success")
        if(req['filter']=='Collaborative Based'):
            return render_template("home.html",ask="colab")

        else:
            return render_template("home.html")

if __name__=='__main__':
    print("Server Initialized")
    app.run(debug=True)