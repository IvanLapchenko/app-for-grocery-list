from flask import Flask


app = Flask(__name__)

from grocery_list import routes

app.secret_key = "QWEty987123"
