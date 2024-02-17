from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


## for testing purposes
import app.manager.PDFHandler as PDFHandler
from summarizers import extract_sum


app = Flask(__name__)

@app.route("/")
def mainPage():
    
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)
    
    
    
   
    
    pass