from data import get_data
from preprocess.preprocess_data import preprocess_pipeline
from gensim import models

data = get_data.akt_naslov_list()  # get data from api
bag_of_words = preprocess_pipeline(data)  # transform a list of documents to a bag of words model

tfidf = models.TfidfModel(bag_of_words)  # create tf-idf matrix
