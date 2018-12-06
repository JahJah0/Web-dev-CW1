#python for 404 page
from website import *

#errorhandler 404
@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404