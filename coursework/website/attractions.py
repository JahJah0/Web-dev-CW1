#python for attractions page
from website import *

#route 127.0.0.1:5000/attractions
@app.route('/attractions')
def attractionPage():
	return render_template('attractions.html')