import nltk
import string
import re
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download("punkt") 
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("stopwords") 

text = "$The quick brown foxes,   jumping over lazy dogs! Isn't it amazing?"

# boşlukları kaldır
remove_spaces = " ".join(text.split())

# büyük küçük harf
lower_text = remove_spaces.lower()

# noktalama işaretlerini kaldır
marks_remove = lower_text.translate(str.maketrans("", "", string.punctuation))

# özel karakterleri kaldır
remove_special_characters = re.sub(r"[^A-Za-z0-9\s]", "", marks_remove)

# tokenize et
word_tokens = nltk.word_tokenize(remove_special_characters)

# köke indirgeme
stemmer = PorterStemmer()
stems = [stemmer.stem(w) for w in word_tokens]

# lemmatizasyon
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(w, pos="v") for w in word_tokens]

# stop word kaldırma
stop_words = set(stopwords.words("english"))
text_list = lemmas
filtered_words = [word for word in text_list if word not in stop_words]

print("Orijinal:", text)
print("Tokenlar:", word_tokens)
print("Kökler (Stems):", stems)
print("Lemmas:", lemmas)
print("Stop word'ler kaldırıldıktan sonra:", filtered_words)
