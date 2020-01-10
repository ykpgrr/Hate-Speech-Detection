import os
import pickle
import re
import string

from flask import Flask, request, jsonify

CUR_DIR = os.path.dirname(__file__)

STOP_WORDS = pickle.load(open(
    os.path.join(CUR_DIR,
                 'pkl_objects',
                 'stopwords.pkl'), 'rb'))
VECTORIZER = pickle.load(open(
    os.path.join(CUR_DIR,
                 'pkl_objects',
                 'vectorizer.pkl'), 'rb'))

CLF = pickle.load(open(
    os.path.join(CUR_DIR,
                 'pkl_objects',
                 'classifier.pkl'), 'rb'))
LABEL_DICT = {0: 'The tweet contains hate speech',
              1: 'The tweet is not offensive',
              2: 'The tweet uses offensive language but not hate speech'}

app = Flask(__name__)


def preprocess_tweet(tweet):
    tweet = tweet.lower()
    # Remove urls
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', tweet)
    # Remove usernames
    tweet = re.sub('@[^\s]+', '', tweet)
    # Remove white space
    tweet = tweet.strip()
    # Remove hashtags
    tweet = re.sub(r'#([^\s]+)', '', tweet)
    # Remove stopwords
    tweet = " ".join([word for word in tweet.split(' ') if word not in STOP_WORDS])
    # Remove punctuation
    tweet = "".join(l for l in tweet if l not in string.punctuation)

    return tweet


@app.route("/analyse/sentiment", methods=['POST'])
def classify_tweet():
    sentence = request.get_json()['sentence']
    sentence_to_clf = preprocess_tweet(sentence)
    sentence_to_clf = VECTORIZER.transform([sentence_to_clf])
    label = CLF.predict(sentence_to_clf)[0]
    confidence = max(CLF.predict_proba(sentence_to_clf)[0]) * 100

    return jsonify(
        sentence=LABEL_DICT[label],
        polarity=confidence
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
