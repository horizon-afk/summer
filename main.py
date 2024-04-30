from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os


import app.manager.PDFHandler as PDFHandler
from summarizers import abstrat


UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


    
@app.route("/", methods=["POST","GET"])
def home():
    text = ""
    summary = ""
    
    #when a POST request is made to the website
    if request.method == 'POST':
        
        #when user wants to upload a PDF
        if request.form['action'] == "Upload":
            f = request.files['file']
            secure_file = secure_filename(f.filename)
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_file))
        
            path_to_file = "uploads/"+ secure_file
            pdf = PDFHandler.PDFReader(path_to_file) #extracts text from a custom made PDF parser
            text = pdf.text()
            os.remove(path_to_file)
            
        #when user wants the text to be processed  
        elif request.form['action'] == "Summary":
            text = request.form.get('text')  
        
        #summarizes the text based on the data fed
        summary = abstrat.summarize(text)
        
    #when a GET request is made to the website on startup
    if request.method == 'GET':
        summary= ""
        
    return render_template('home.html', summary = summary)
    
#main entry point of the app
if __name__ == "__main__":
    
    with app.app_context():      
        app.run()
