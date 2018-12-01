#python for book room page
from website import *

@app.route('/bookroom')
def bookingPage():
	return render_template('bookroom.html')