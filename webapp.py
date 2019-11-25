import os
import connexion
from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import requests

CUR_DIR = os.path.dirname(__file__)

app = connexion.App(__name__, specification_dir='./')
# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')
API_ENDPOINT = "http://0.0.0.0:5000/api/clf_0"


class ReviewForm(Form):
    tweet_classifier = TextAreaField('',
                                     [validators.DataRequired(),
                                      validators.length(min=5)])


@app.route('/')
def index():
    form = ReviewForm(request.form)
    return render_template('mainpage.html', form=form)


@app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        tweet = request.form['tweet_classifier']
        response = requests.post(url=API_ENDPOINT, json=tweet).json()
        y = response["label"]
        probability = response["confidence"]
        return render_template('resultpage.html',
                               content=tweet,
                               prediction=y,
                               probability=probability)
    return render_template('mainpage.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
