### Hate Speech Detection for tweets
###### Yakup Görür @ykpgrr yakup.gorur@gmail.com https://github.com/ykpgrr

> Developing an application for hate speech detection<br>
> offensive language detection for tweet texts.<br><br>
> `docker pull ykpgrr/hate_speech_detection_tweet` <br><br>
> This application run on a basic flask web server communicate with backend `model.py` using REST.<br><br>
> To illustrate REST API `connexion` library is used. `connexion` maps the endpoints to Python functions.<br>
> Any security measures does not used. usage of Secret-Key is recommended for REST API <br><br>
> in `model.py` there are 3 steps: preprocess the tweets, word embedding (vectorizer), classification. All steps depend on their pickle files.<br><br>

 workingspace, data and notebooks can be found in path `./notebooks/` <br>
