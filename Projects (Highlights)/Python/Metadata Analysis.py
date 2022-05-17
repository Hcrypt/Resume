import os, pyPdf        # import both os and pyPdf module
from pyPdf import PdfFileReader         # import PdfFileReader object from pyPdf module

targ_dir = raw_input("Path: ")          # instead of input(), used raw_input() to grab input as string (variable is called "targ_dir")
file_names = os.listdir(targ_dir)           # create a variable called "file_names" and when called, use listdir function in os module to create a list of object containing the filename from our target directory
f = open('./VangBee_11.7.2019.txt', 'w')

def getPDFdata (PDFFile):                   # define "getPDFdata" as a function with "PDFFile" as a parameter to later be callable as an arguement
# What's inside () is called a "parameter" when you define a function. It's called an "argument" when you call the function.
    pdf = PdfFileReader(file(PDFFile, 'rb'))    # when "PDFFile" is called, then the "PdfFileReader" function will read "PDFFile" as binary (variable is called "pdf")
    if pdf.isEncrypted:             # if the variable "pdf" gets called and the first is encrypted, then decrypt it.
	    pdf.decrypt('')
    metadata = pdf.getDocumentInfo()    # using the getDocumentInfo() function, pull the pdf file and store it as the variable called "metadata"
#    pdf.getFormTextFields()
    print PDFFile               # print the "getPDFdata" function we just defined
    for info in metadata:       # Create for loop incase their is an error as pulling from metadata
	    try:
	    	print info+"::"+metadata[info]           # Each time the code is ran based off the number of metadata (basically the number of files) try to run data pulled from "info" with "metadata" information
                f.write(info+"::"+metadata[info] + '\r')
#                f.write("_"*30 + "\n")              # Not meant to be here, gonna move it to the end of the loop
	    except UnicodeEncodeError:
    		print "Error"              # Each loop, if their is an error, print this.
    print "_"*30
    f.write("_"*30 + "\n")             # After the entire loop ends, print this. This is to seperate each metadata from the other

for item in file_names:                              # Create a for loop "item" in call the "file_names" variable we created before
    meta = getPDFdata(targ_dir+"\\"+item)                   # Each time the code is ran based off the number of files, use the "getPDFdata" function we created before to call the variable/arguement "targ_dir" and "item" that we created before
#    print ("---------------")           # Wrote this here as part of my debugging process to test where the program is hung up at
