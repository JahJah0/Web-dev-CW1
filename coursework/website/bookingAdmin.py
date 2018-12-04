#python for admin booking page
from website import *
from flask import request
from flask import Flask,redirect
import csv

#admin booking page
@app.route('/booking/admin', methods=['GET', 'POST'])
def bookingPageAdmin():
    return displayBooking()

#confirm a booking    
@app.route('/booking/admin/confirm', methods=['POST'])
def confirmBooking():
    file = os.path.join(APP_CSV, 'bookings.csv')
    bookingFile = readFile(file)
    
    lineIndex = request.form['confirm']
    
    index = int(lineIndex)
    line = bookingFile[index]
    newEntry = line[-1].replace("REQUEST", "CONFIRMED")
    newEntry = [line[0], line[1], newEntry]
    
    bookingFile.remove(line)
    bookingFile.append(newEntry)
    writeFile(bookingFile, file)
            
    return redirect("/booking/admin", code=302)

#deny a booking    
@app.route('/booking/admin/deny', methods=['POST'])
def denyBooking():
    file = os.path.join(APP_CSV, 'bookings.csv')
    bookingFile = readFile(file)
    
    lineIndex = request.form['deny']
    
    index = int(lineIndex)
    line = bookingFile[index]
    newEntry = line[-1].replace("REQUEST", "DENIED")
    newEntry = [line[0], line[1], newEntry]
    
    bookingFile.remove(line)
    bookingFile.append(newEntry)
    writeFile(bookingFile, file)
    
    return redirect("/booking/admin", code=302)

#display booking requests
def displayBooking():
    file = os.path.join(APP_CSV, 'bookings.csv')
    bookingFile = readFile(file)
    return render_template('bookingAdmin.html', bookingFile=bookingFile)
    
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