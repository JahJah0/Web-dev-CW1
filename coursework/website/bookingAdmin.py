#python for admin booking page
from website import *

#admin booking page
#route 127.0.0.1:5000/booking/admin
@app.route('/booking/admin', methods=['GET', 'POST'])
def bookingPageAdmin():
    return displayBooking()

#confirm a booking 
#route 127.0.0.1:5000/booking/admin/confirm   
@app.route('/booking/admin/confirm', methods=['POST'])
def confirmBooking():
    file = os.path.join(APP_CSV, 'bookings.csv')
    bookingFile = readFile(file)
    #assigns line index value so the line can be accessed
    #changes the booking status for the line to confirmed
    lineIndex = request.form['confirm']
    index = int(lineIndex)
    line = bookingFile[index]
    dateStart = line[2]
    dateEnd = line[3]
    
    for row in bookingFile:
        if (row[2] == dateStart or row[3] == dateStart or row[2] == dateEnd or row[3] == dateEnd) and row[-1] == "CONFIRMED":
            flash('Booking request not confirmed. Request dates conflict with a confirmed booking.')
            return redirect(url_for('bookingPageAdmin'))
    
    newEntry = line[-1].replace("REQUEST", "CONFIRMED")
    newEntry = [line[0], line[1], line[2], line[3], newEntry]
    #removes the old line and replaces it in 'bookings.csv'
    bookingFile.remove(line)
    bookingFile.append(newEntry)
    writeFile(bookingFile, file)
    #returns to previous page        
    flash('Booking confirmed.')
    return redirect(url_for('bookingPageAdmin')) 

#deny a booking  
#route 127.0.0.1:5000/booking/admin/deny  
@app.route('/booking/admin/deny', methods=['POST'])
def denyBooking():
    file = os.path.join(APP_CSV, 'bookings.csv')
    bookingFile = readFile(file)
    #assigns line index value so the line can be accessed
    #changes the booking status for the line to denied
    lineIndex = request.form['deny']
    index = int(lineIndex)
    line = bookingFile[index]
    newEntry = line[-1].replace("REQUEST", "DENIED")
    newEntry = [line[0], line[1], line[2], line[3], newEntry]
    #removes the old line and replaces it in 'bookings.csv'
    bookingFile.remove(line)
    bookingFile.append(newEntry)
    writeFile(bookingFile, file)
    #returns to previous page
    flash('Booking denied.')
    return redirect(url_for('bookingPageAdmin')) 

#clears everything from 'bookings.csv'
@app.route('/booking/admin/clearAll')
def clearAllBookings():
    file = os.path.join(APP_CSV, 'bookings.csv')
    open(file, 'w').close()
    flash('All bookings cleared.')
    return redirect(url_for('bookingPageAdmin')) 

#clears all bookings with "DENIED"
@app.route('/booking/admin/clearDenied')
def clearDeniedBookings():
    file = os.path.join(APP_CSV, 'bookings.csv')
    bookingFile = readFile(file)

    for line in bookingFile:
        if line != bookingFile[-1]:
            if line[-1] == "DENIED":
                bookingFile.remove(line)
    
    writeFile(bookingFile, file)
    flash('All denied bookings cleared.')
    return redirect(url_for('bookingPageAdmin'))    
   
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