from flask import Flask, render_template
from flask import request
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_CSV = os.path.join(APP_ROOT, 'csv')
