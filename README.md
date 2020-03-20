# Project: Using Classification Models to Predict Posts From r/StarWars vs. r/startrek
## Problem Statement

In this project, I developed multiple classification models to predict which of
the following subreddits a given post belongs to: r/startrek or r/StarWars. The
project relies on various natural language processing (NLP) techniques to process text
information of a post. 

The following classification models were developed: Naive Bayes (Multinomial Naive
Bayes and Gaussian Naive Bayes), Logistic Regression, KNN, and SVM. The AUC ROC
score was used as the metric for model evaluation and selection.

5000 posts from each subreddit (r/startrek and r/StarWars) were collected using
[Pushshift's](https://pushshift.io/api-parameters/).


---

## Executive Summary

During the data collection process, I noticed that in order to collect the same amount of posts (i.e. 5000 for each subreddit), r/StarWars went over a much longer time span (780 days), comparing to r/startrek which only went over 420 days. Since our function only collects 'is_self' (i.e. text posts), This information indicated that r/startrek posts tend to have more text posts than r/StarWars. However, this information was not included in the features for our models, and we should keep in mind of the limitation of our models.

During the EDA and data cleaning process, I used techniques such as tokenizing, lemmatizing, and creating custom stop words to preprocess our text data. I also engineered a feature to combine the title and the body of the post in order to maximize the amount of text information to train our models. These steps have improved our models' performance.

During the modeling process, I used pipelines combined with grid-search for each model. I was especially interested in exploring the different results between using CountVectorizer vs. TFIDF: the former counts the occurrence of the words, where as the latter penalizes a word if it occurs often across the corpus and documents. I also tuned the models using a variety of hyper-parameters. I started with the Naive Bayes models, since I assumed that the models are simple and fast. I then explored more complex models such as logistic regression, KNN, and SVM. Does more complex and sophisticated models yield the best result? let's find out!

---

## Conclusion

Among the 4 categories of models, i.e. Naive Bayes, Logistic Regression, KNN, and SVM, the simple Multinomial Naive Bayes outperformed the others by a very small margin. Based on the AUC ROC score, the model is able to provide a very good threshold to separate the two classes, i.e. r/startrek and r/StarWars. In addition, Multinomial Naive Bayes runs faster than the others.

I conclude that this model is sufficient to be used as part of the bot to make
suggestions about a subreddit (i.e. r/startrek or r/StarWars) to crosspost to
based on the title and contents of the posts.

---
## Limitations

during the data collection process, important information was left out: Since we
only collect posts with text, r/startrek have more of posts with text than
r/StarWars. Our function was able to collect 5000 posts for r/startrek for the
timespan of 420 days; in contrast, in order to collect the same amount of posts,
r/StarWars need a timespan of 780 days. This information could be an important
predictor that we fail to consider at this time. 

The data we use to train the model do not include the comments. As we know,
reddit comments are the goldmine where we can find a lot of valuable
information. To further improve our model, we should consider including comments
in our dataset. 

