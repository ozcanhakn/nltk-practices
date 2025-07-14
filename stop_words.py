import nltk

from nltk.corpus import stopwords

nltk.download("stopwords") # farklı dillerde en çok kullanılan stop words veri seti


# ingilizce stop words analizi
stop_words_eng = set(stopwords.words("english"))

text = "There are some examples of handling stop words from some texts."

text_list = text.split()

filtered_words = [word for word in text_list if word.lower() not in stop_words_eng]


# %%
# Türkçe stop words analizi

import nltk

from nltk.corpus import stopwords

nltk.download("stopwords")

stop_words_tr = set(stopwords.words("turkish"))

text = "selam arkadaşlar çok güzel bir pratik yapıyoruz"

text_list_tr = text.split()

filtered_words_tr = [word for word in text_list_tr if word.lower() not in stop_words_tr]













