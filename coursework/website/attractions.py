#python for attractions page
from website import *

@app.route('/attractions')
def attractionPage():
	return render_template('attractions.html')