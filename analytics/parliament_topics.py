from data import get_data
from preprocess.preprocess_data import preprocess_pipeline
from gensim import models
from time import time


if __name__ == '__main__':
    start_t = time()
    data = get_data.akt_naslov_list()  # get data from api
    bag_of_words = preprocess_pipeline(data)  # transform a list of documents to a bag of words model
    tfidf = models.TfidfModel(bag_of_words)  # create tf-idf matrix

    print(time()-start_t)
