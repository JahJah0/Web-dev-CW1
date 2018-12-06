from flask import Flask, render_template, request, redirect, flash, url_for
import os
import csv
import datetime

app = Flask(__name__)

app.secret_key = 'secretkey'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_CSV = os.path.join(APP_ROOT, 'csv')