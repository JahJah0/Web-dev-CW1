#python for booking page
from website import *
from flask import request
import csv

#standard booking page
@app.route('/booking', methods=['GET','POST'])
def bookingPage():
    if request.method == 'POST':
        addBooking()
        return render_template('booking.html')
    else:
        return render_template('booking.html')

#add booking request    
def addBooking():
    file = os.path.join(APP_CSV, 'bookings.csv')
    bookingFile = readFile(file)
    
    nameIn = request.form['name']
    emailIn = request.form['email']
    
    if nameIn == "" or emailIn == "":
        return
    else:
        newEntry = [nameIn, emailIn, "REQUEST"]
        bookingFile.append(newEntry)
        writeFile(bookingFile, file)
        return render_template('booking.html', bookingFile=bookingFile)        
         
#read csv file
def readFile(aFile):
    with open(aFile, 'r') as inFile:
        reader = csv.reader(inFile)
        reader = [row for row in reader]
    return reader
        
#write to csv file
def writeFile(aList, aFile):
    with open(aFile, 'w', newline="") as outFile:
        writer = csv.writer(outFile)
        writer.writerows(aList)
    return