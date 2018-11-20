from flask import Flask, render_template
from flask import request
main = Flask(__name__)

@main.route('/')
def home():
	return render_template('home.html')


if __name__ == '__main__':
    main.run(debug = True)