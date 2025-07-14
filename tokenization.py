import nltk

nltk.download("punkt") # metni kelime ve cumle bazinda ayirabilmek icin gereklidir.
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

text = "Hello,  World! How are you? Hello, hi ..."


# Kelime tokenizasyonu: word_tokenize: metni kelimelere ayırır,
# noktalama işaretleri ve boşluklar ayrı birer token olarak elde edilecektir
word_tokens = nltk.word_tokenize(text)

# cumle tokenizasyonu sent_tokenize: metni cümlelere ayırır. her bir cümle birer token olur
sentence_tokens = nltk.sent_tokenize(text)
