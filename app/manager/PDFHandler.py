#this module is custom made to let other front end devs unerstand how
#the pdf is read by pyhton and not worry about much of the backend
#if they wish to edit it, they can refer to the docs at https://pypdf.readthedocs.io/en/stable/
#! WARNING: DO NOT EDIT THIS FILE IF YOU DON'T WANT TO MANAGE PDFs AS IT MAY BREAK THE PDF FEATURE
from pypdf import  PdfReader, PdfWriter


# **limitation: only works on purely text based documents
# **reads only one page

class PDFReader:
    file = None
    
    #TODO: Check and manage if entered pdf has more than one page since it won't be readable
    
    
    def __init__(self, filename: str) -> None:
        self.file = PdfReader(filename)
      
        
        
    def text(self):
        reader = self.file
        extract = reader.pages[0]
        content = extract.extract_text()
        return content
    

        
        
        
        
      
   
# testFileReader = PDFReader("text_files/test.pdf")
# print(testFileReader.text())
