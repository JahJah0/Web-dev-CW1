from website import *

@app.route('/test')
def testPage():
	return render_template('test.html')