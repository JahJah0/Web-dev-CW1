#python for homepage
from website import *

#route 127.0.0.1:5000/
@app.route('/')
def homePage():
    
    return render_template('home.html')
