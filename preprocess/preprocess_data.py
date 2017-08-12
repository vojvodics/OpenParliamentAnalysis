"""
This file contains methods for preprocessing text.
The intendet pipeline would be:
    1. s = get_stemmed_list_of_documents(list_of_documents)  # parsing one document at a time
    2. d = create_dictionary(s)
    3. m = create_document_term_matrix(d, s)  # bag of words
"""

from preprocess.stemmers.Croatian_stemmer import stem_list as CroStemmer
from nltk.tokenize import word_tokenize
from preprocess.stop_words import stop_words
from gensim import corpora

# test_docs = ['Na sednici Odbora za ustavna pitanja i zakonodavstvo, održanoj 14. jula, utvrđen je Predlog za izbor ',
#              'Zaštitnika građana.\r\n\r\nNarodna skupština, na predlog Odbora za ustavna pitanja i zakonodavstvo, ',
#              'bira Zaštitnika građana, a kandidate Odboru predlažu poslaničke grupe Narodne skupštine.',
#              '\r\n\r\nPredlog da se za Zaštitnika građana izabere kandidat Ekaterina Marinković, podnela je ',
#              'Poslanička grupa Srpska radikalna stranka; predlog da se za Zaštitnika građana izabere zajednički ',
#              'kandidat Miloš Janković, podneli su Poslanička grupa Demokratska stranka i Poslanička grupa ',
#              'Socijaldemokratska stranka - Narodni pokret Srbije; predlog da se za Zaštitnika građana izabere ',
#              'zajednički kandidat Zoran Pašalić, podnele su poslaničke grupe Srpska napredna stranka, ',
#              'Pokret socijalista - Narodna seljačka stranka - Ujedinjena seljačka stranka, ',
#              'Socijalistička partija Srbije, Socijaldemokratska partija Srbije, Jedinstvena Srbija, Partija ',
#              'ujedinjenih penzionera Srbije i Savez vojvođanskih Mađara - Partija za demokratsko delovanje, i predlog ',
#              'da se za Zaštitnika građana izabere kandidat Vojin Biljić, podnela je Poslanička grupa ',
#              'Dosta je bilo.\r\n\r\nNakon obavljenih razgovora sa kandidatima, članovi Odbora su većinom ',
#              'glasova uputili predlog Narodnoj skupštini da za Zaštitnika građana izabere Zorana Pašalića, ',
#              'po hitnom postupku. \r\n\r\nSednici je predsedavao predsednik Odbora Đorđe Komlenski, ',
#              'a prisustvovali su sledeći članovi i zamenici članova Odbora: Vesna Nikolić Vukajlović, ',
#              'Krsto Janjušević, Zoran Krasić, Bojan Torbica, Saša Radulović, Jelena Žarić Kovačević, ',
#              'Dejan Šulkić, Aleksandra Majkić, Srbislav Filipović, Vojislav Vujić, Nataša Vučković, ',
#              'Balint Pastor i Jasmina Obradović.']


def get_stemmed_document_list(text):
    """
    Method for converting raw text to list of stemmed tokens.
    :param text: raw text
    :return: list of preprocessed tokens
    """
    # Get list of tokens
    tokens = word_tokenize(text.lower())
    # Remove stop words
    stop_tokens = [token for token in tokens if token not in stop_words]
    # Stemming
    stemmed_tokens = CroStemmer(stop_tokens)
    return stemmed_tokens


def get_stemmed_list_of_documents(list_of_documents):
    """
    Method for converting list of documents 
    :param list_of_documents: e.g. ['tomato potato', 'salad soup meat', ...]
    :return: list of stemmed document lists e.g. [['tomat', 'potat'], ['salad', 'sou', 'mea'] ...]
    """
    dictionary = [get_stemmed_document_list(text) for text in list_of_documents]
    return dictionary


def create_dictionary(list_of_tokenized_documents, save=False, print_dict=False):
    """
    Method for creating tokenized documents into a id <-> term dictionary
    :param list_of_tokenized_documents: list of stemmed document lists e.g. [['tomat', 'potat'], ['salad', 'sou', 'mea'] ...]
    :param save: if True, saves the document in temp folder
    :param print_dict: prints id <-> terms
    :return: id <-> term dictionary
    """
    dictionary = corpora.Dictionary(list_of_tokenized_documents)
    if save is True:
        try:
            with open('../temp/dictionary.txt', 'wb') as f:
                dictionary.save(f)
        except IOError:
            print("Couldn't save dictionary to temp folder :(")

    if print_dict is True:
        print(dictionary.token2id)
    return dictionary


def create_document_term_matrix(dictionary, list_of_tokenized_documents):
    """
    Method for creating bag of words model.
    
    :param dictionary: id <-> term dictionary
    :param list_of_tokenized_documents: 
    :return: list of stemmed document lists e.g. [['tomat', 'potat'], ['salad', 'sou', 'mea'] ...]
    """
    dt_matrix = [dictionary.doc2bow(text) for text in list_of_tokenized_documents]
    return dt_matrix


def preprocess_pipeline(list_of_documents):
    tokenized_doc_list = get_stemmed_list_of_documents(
        list_of_documents)  # process list of documents -> doc = list of stemmed words
    dictionary = create_dictionary(tokenized_doc_list)
    bow = create_document_term_matrix(dictionary, tokenized_doc_list)
    return bow
