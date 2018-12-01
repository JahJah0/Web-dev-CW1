#from website folder import the following .py files
from website import app, APP_CSV, homepage, attractions, bookroom, review, test

#debug
if __name__ == '__main__':
    app.run(debug = True)