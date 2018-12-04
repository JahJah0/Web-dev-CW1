#python for reviews page
from website import *
from flask import request
import datetime
import csv

#if the request method is POST 
@app.route('/review', methods=['GET', 'POST'])
def reviewPage():
    if request.method == 'POST':
        addReview()
        return displayReview()
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
    
    nameIn = request.form['name']
    reviewIn = request.form['review']
    ratingIn = request.form['rating']
    
    time = datetime.datetime.now()
    formatTime = time.strftime("%H:%M %d-%m-%Y")
    
    if nameIn == "" or reviewIn == "":
        return
    else:
        newEntry = [nameIn, reviewIn, ratingIn + "/5", formatTime]
        reviewsFile.append(newEntry)
        writeFile(reviewsFile, file)
        return render_template('review.html', reviewsFile=reviewsFile)

#read file
def readFile(aFile):
    with open(aFile, 'r') as inFile:
        reader = csv.reader(inFile)
        reader = [row for row in reader]
    return reader

#write to file
def writeFile(aList, aFile):
    with open(aFile, 'w', newline="") as outFile:
        writer = csv.writer(outFile)
        writer.writerows(aList)
    return
    
