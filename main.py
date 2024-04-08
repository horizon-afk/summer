from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app.database.shared import db
from app.route import route
from werkzeug.utils import secure_filename
import os


## for testing purposes
import app.manager.PDFHandler as PDFHandler
from summarizers import extract_sum, abstrat


UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db.init_app(app)


@app.route("/", methods=["POST","GET"])
def main():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(f.filename)))
    
        return 'file uploaded'
        
    if request.method == 'GET':
        return render_template('index.html')
    
    
@app.route("/home", methods=["POST","GET"])
def home():
    
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(f.filename)))
        
        path_to_file = "uploads/"+ f.filename
        pdf = PDFHandler.PDFReader(path_to_file)
        text = pdf.text()
        os.remove(path_to_file)
        
        summary = abstrat.summarize(text)
        
        
        return render_template('home.html', summary = summary)
    
    
    if request.method == 'GET':
        summary= ""
        ## clear the upload direectory
        return render_template('home.html')
    

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
            



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS          

        





if __name__ == "__main__":
    
    
    with app.app_context():
        db.create_all()
        app.run(debug=True)
        
    
    
    
   
    
    pass