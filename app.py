from flask import Flask, render_template, request
from langdetect import detect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict.html', methods=['POST'])
def predict():
    text = request.form['langInput']
    language = detect(text)


    if text  is not None:
        return f"The detected language is: {language}"
    else:
        return "no language inputted"
    

if __name__ == '__main__':
    app.run()
