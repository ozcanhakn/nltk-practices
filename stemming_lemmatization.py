import nltk

nltk.download("wordnet") # wordnet: lemmatizatin için gerekli veri tabanı

from nltk.stem import PorterStemmer #stemming için fonksiyon

# porter stemmer modelini oluştur.

stemmer = PorterStemmer()

words = ["running","runner", "ran", "runs", "went", "go", "better"]


stems = [stemmer.stem(w) for w in words]

# %%

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["running","runner", "ran", "runs", "went", "go", "better"]

lemmas = [lemmatizer.lemmatize(w, pos="v") for w in words]