#python for booking page
from website import *

#standard booking page
#route 127.0.0.1:5000/booking
@app.route('/booking', methods=['GET','POST'])
def bookingPage():
    if request.method == 'POST':
        addBooking()
        return displayBooking()
    else:
        return displayBooking()

#add booking request    
def addBooking():
    file = os.path.join(APP_CSV, 'bookings.csv')
    bookingFile = readFile(file)
    #assigns form values
    nameIn = request.form['name']
    emailIn = request.form['email']
    dateStart = request.form['start']
    dateEnd = request.form['end']
    #gets current date and time
    currentDate = datetime.datetime.now()
    currentDate = currentDate.strftime("%Y-%m-%d")
    #check if form fields are empty shows error if necessary
    if nameIn == "" or emailIn == "" or dateStart == "" or dateEnd == "":
        flash('Invalid booking request. Fields cannot be empty.')
        return render_template('booking.html')
    #checks that start date is >= todays date and end date is > start date. shows error if necessary
    elif dateStart < currentDate or dateEnd <= dateStart:
        flash('Invalid booking request. Input vaild dates.')
        return render_template('booking.html')
    else:
        #for each line in booking file check if the dates conflict with confirmed bookings
        for line in bookingFile:
            if (line[2] == dateStart or line[3] == dateStart) and line[-1] == "CONFIRMED":
                flash('Invalid booking request. The start date is not availiable.')
                return render_template('booking.html')
            elif (line[2] == dateEnd or line[3] == dateEnd) and line[-1] == "CONFIRMED":
                flash('Invalid booking request. The end date is not availiable.')
                return render_template('booking.html')
        #adds booking details to 'bookings.csv'
        newEntry = [nameIn, emailIn, dateStart, dateEnd, "REQUEST"]
        bookingFile.append(newEntry)
        writeFile(bookingFile, file)
        flash('Booking request was made.')
        return render_template('booking.html', bookingFile=bookingFile)

#displays booking.html with 'booking.csv' data
def displayBooking():
    file = os.path.join(APP_CSV, 'bookings.csv')
    bookingFile = readFile(file)
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