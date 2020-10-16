import pyttsx3
import PyPDF2


# Audio function for the program
def speak(audio):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150)
    engine.say(audio)
    engine.runAndWait()


# Function to read text from pdf
def read(pdf_name,num):
    pdf_obj=PyPDF2.PdfFileReader(pdf_name)
    string=pdf_obj.getPage(num).extractText()
    speak(string)

# User Input PDF Name
pdf_name=input("Enter the name of pdf: ")
# User Input Page number of pdf
page_number=int(input("Enter page number of the pdf : "))
# Open Object for file open
open_pdf=open(pdfname,'rb')
# Read Object for file reading
read(open_pdf,page_number)
# ckose Object for file Close
open_pdf.close()
