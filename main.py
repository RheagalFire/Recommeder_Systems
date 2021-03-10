from flask import Flask,request,jsonify,render_template
import model
import os
from sqlalchemy import create_engine
try:
    DB_KEY=os.environ["DATABASE_URL"]
except:
    from dotenv import load_dotenv
    load_dotenv()
    DB_KEY=os.getenv("DATABASE_URL")
engine = create_engine(DB_KEY)
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
                for j in obj[0][1:]:
                    strings.append(j)
                return render_template("home.html",movie=index[0],r=strings,ask="success_2")
        if(req['filter']=='Collaborative Based'):
            return render_template("home.html",ask="colab")

        else:
            return render_template("home.html")

if __name__=='__main__':
    print("Server Initialized")
    app.run(debug=True)