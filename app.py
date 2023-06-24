# from flask import Flask, request,render_template
# import pickle

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "hello guys"

# app.run(port=5000)

from flask import Flask, request,render_template
from langdetect import detect

app = Flask(__name__)

# text = "Hello, how are you?"

# language = detect(text)

# print(f"The detected language is: {language}")

@app.route('/')
def home():
    text = "Hello, how are you?"
    language = detect(text)

    print(f"The detected language is: {language}")

app.run(port=5000)

