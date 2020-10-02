import pyttsx3
import PyPDF2

#audio function for the program
def speak(audio):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150)
    engine.say(audio)
    engine.runAndWait()

#function to read text from pdf
def read(pdf_name,num):
    pdf_obj=PyPDF2.PdfFileReader(pdf_name)
    string=pdf_obj.getPage(num).extractText()
    speak(string)

pdfname=input("Enter the name of pdf: ")
page_number=int(input("Enter page number of the pdf : "))
open_pdf=open(pdfname,'rb')
read(open_pdf,page_number)
open_pdf.close()