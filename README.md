### Hate Speech Detection for tweets
###### Yakup Görür @ykpgrr yakup.gorur@gmail.com https://github.com/ykpgrr

Developing an application for hate speech detection<br>
offensive language detection for tweet texts.<br><br>

:heavy_check_mark: From docker hub: <br/>
`docker pull ykpgrr/hate_speech_detection_tweet` <br><br>

:heavy_check_mark: There are also k8s configuration files on [kubernetes branch](https://github.com/ykpgrr/Hate-Speech-Detection/tree/kubernetes)

 - This application run on a basic flask web server communicate with backend `model.py` using REST.<br>

- To illustrate REST API `connexion` library is used. `connexion` maps the endpoints to Python functions.<br>

- Any security measures does not used. usage of Secret-Key is recommended for REST API <br><br>

- in `model.py` there are 3 steps: preprocess the tweets, word embedding (vectorizer), classification. All steps depend on their pickle files.<br><br>

## Machine Learning Model
Key concepts: 
- Dataset consist of two parts as train and test sets.
 - Train dataset: 19826 sentences  (~%85)
 - Test dataset: 3878 sentences (~%15)
 - Sentences are labeled as ’hate speech’ (label=0), ’offensive language’ (label=1) or ’neither’ (label=2).
- Preprocess applied on sentences.
 - Stopwords are removed.
 - Exclusion words are removed.
 - Words are tokenized.
- Feature generation methods are applied on sentences
 - Tfidf features are generated.
 - Counter of words features are generated.
 - Number of word, number of unique words, and character based embeddings are generated.
- Model trained.
 - LinearSVM, Logistic Regression, and GridSearch methods are used.
- Evaluation:
 - F1 score: %85 <br />

![model_evaluation](docs/model_evaluation.png)

:heavy_check_mark: workingspace, data and notebooks can be found under [Notebooks](Notebooks/) <br>
