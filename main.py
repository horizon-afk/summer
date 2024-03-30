from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app.database.shared import db
from app.route import route


## for testing purposes
import app.manager.PDFHandler as PDFHandler
from summarizers import extract_sum


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/login', methods=["POST","GET"])
def login():
    
    if request.method == "GET":
        return render_template('log.html')
    
    elif request.method == "POST":
        session = "login"

        if session == "signup": 
            name = request.args.get("uname_signup")    
            email = request.args.get("email_signup")
            password = request.args.get("pass_signup")
        
        elif session == "login":
   
            name = request.args.get("uname_login")
            password = request.args.get("pass_login")
            
            
            
        
        
    
        
        


# @app.route('/home')
# def home():
#     return




if __name__ == "__main__":
    
    
    with app.app_context():
        db.create_all()
        app.run(debug=True)
        
    # pdf = PDFHandler.PDFReader("text_files/halo.pdf")
    # text = pdf.text()
    # print(extract_sum.summarize(text,0.5))
    
    
   
    
    pass