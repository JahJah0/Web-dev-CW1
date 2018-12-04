#python for homepage
from website import *

@app.route('/')
def homePage():
    
    return render_template('home.html')
