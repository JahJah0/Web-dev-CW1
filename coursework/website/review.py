#python for reviews page
from website import *
from flask import request
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
    
    nameIn = request.form[('name')]
    reviewIn = request.form[('review')]
    ratingIn = request.form[('rating')]
    
    if nameIn == "" or reviewIn == "":
        return
    else:
        newEntry = [reviewIn, " " + ratingIn + "/5", " - " + nameIn]
        reviewsFile.append(newEntry)
        writeFile(reviewsFile, file)
        return render_template('review.html', reviewsFile=reviewsFile)

#
def readFile(aFile):
    with open(aFile, 'r') as inFile:
        reader = csv.reader(inFile)
        reader = [row for row in reader]
    return reader

#
def writeFile(aList, aFile):
    with open(aFile, 'w', newline="") as outFile:
        writer = csv.writer(outFile)
        writer.writerows(aList)
    return
    
