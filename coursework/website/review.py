#python for reviews page
from website import *

#if the request method is POST 
#route 127.0.0.1:5000/review
@app.route('/review', methods=['GET', 'POST'])
def reviewPage():
    if request.method == 'POST':
        return addReview()
    else:
        return displayReview()
    
#reads the reviews.csv file and renders the text on reviews.html
def displayReview():
    file = os.path.join(APP_CSV, 'reviews.csv')
    reviewsFile = readFile(file)
    return render_template('review.html', reviewsFile=reviewsFile)
    
#reads the reviews.csv file and appends the form input, then rerenders review.html
def addReview():
    file = os.path.join(APP_CSV, 'reviews.csv')
    reviewsFile = readFile(file)
    #assigns form values
    nameIn = request.form['name']
    reviewIn = request.form['review']
    ratingIn = request.form['rating']
    #gets current date and time
    time = datetime.datetime.now()
    formatTime = time.strftime("%H:%M %d-%m-%Y")
    #check if form fields are empty shows error if necessary
    if nameIn == "" or reviewIn == "":
        flash('Invalid review. Fields cannot be empty.')
        return redirect(url_for('reviewPage'))
    #else assigns form values and adds to 'bookings.csv'
    else:
        newEntry = [nameIn, reviewIn, ratingIn + "/5", formatTime]
        reviewsFile.append(newEntry)
        writeFile(reviewsFile, file)
        flash('Booking request was made.')
        return render_template('review.html', reviewsFile=reviewsFile)
        
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