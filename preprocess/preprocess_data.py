from preprocess.stemmers.Serbian_stemmer import stem_str as SerbStemmer
from preprocess.stemmers.Croatian_stemmer import stem as CroStemmer
from nltk.tokenize import word_tokenize
from preprocess.stop_words import stop_words

if __name__ == '__main__':
    string = 'Na sednici Odbora za ustavna pitanja i zakonodavstvo, održanoj 14. jula, utvrđen je Predlog za izbor ' \
             'Zaštitnika građana.\r\n\r\nNarodna skupština, na predlog Odbora za ustavna pitanja i zakonodavstvo, ' \
             'bira Zaštitnika građana, a kandidate Odboru predlažu poslaničke grupe Narodne skupštine.' \
             '\r\n\r\nPredlog da se za Zaštitnika građana izabere kandidat Ekaterina Marinković, podnela je ' \
             'Poslanička grupa Srpska radikalna stranka; predlog da se za Zaštitnika građana izabere zajednički ' \
             'kandidat Miloš Janković, podneli su Poslanička grupa Demokratska stranka i Poslanička grupa ' \
             'Socijaldemokratska stranka - Narodni pokret Srbije; predlog da se za Zaštitnika građana izabere ' \
             'zajednički kandidat Zoran Pašalić, podnele su poslaničke grupe Srpska napredna stranka, ' \
             'Pokret socijalista - Narodna seljačka stranka - Ujedinjena seljačka stranka, ' \
             'Socijalistička partija Srbije, Socijaldemokratska partija Srbije, Jedinstvena Srbija, Partija ' \
             'ujedinjenih penzionera Srbije i Savez vojvođanskih Mađara - Partija za demokratsko delovanje, i predlog ' \
             'da se za Zaštitnika građana izabere kandidat Vojin Biljić, podnela je Poslanička grupa ' \
             'Dosta je bilo.\r\n\r\nNakon obavljenih razgovora sa kandidatima, članovi Odbora su većinom ' \
             'glasova uputili predlog Narodnoj skupštini da za Zaštitnika građana izabere Zorana Pašalića, ' \
             'po hitnom postupku. \r\n\r\nSednici je predsedavao predsednik Odbora Đorđe Komlenski, ' \
             'a prisustvovali su sledeći članovi i zamenici članova Odbora: Vesna Nikolić Vukajlović, ' \
             'Krsto Janjušević, Zoran Krasić, Bojan Torbica, Saša Radulović, Jelena Žarić Kovačević, ' \
             'Dejan Šulkić, Aleksandra Majkić, Srbislav Filipović, Vojislav Vujić, Nataša Vučković, ' \
             'Balint Pastor i Jasmina Obradović.'
    tokens = word_tokenize(string.lower())
    stop_tokens = [token for token in tokens if not token in stop_words]
    # stem_string_srb = SerbStemmer(string)
    # stem_string_cro = CroStemmer(string)
    # tokens1 = word_tokenize(stem_string_srb)
    # tokens2 = word_tokenize(stem_string_cro)
    # print(tokens1)
    # print(tokens2)
    # print(tokens)
    # print(stem_string_srb)
    # print(stem_string_cro)
    print(stop_tokens)
