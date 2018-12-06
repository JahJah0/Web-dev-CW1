#from website folder import the following .py files
from website import app, APP_CSV, homepage, attractions, booking, bookingAdmin, review, error

#debug
if __name__ == '__main__':
    app.run(debug = True)