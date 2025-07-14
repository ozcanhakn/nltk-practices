# metinlerde bulunan fazla boşlukları ortadan kaldır

text = "Hello,    World!               2025"

cleaned_text = " ".join(text.split())
print(f"text: {text} \ncleaned_text: {cleaned_text}")

# %%  büyük -> küçük hard çevrimi

text = "Hello, World! 2025"

cleaned_text1 = text.lower()
print(f"text: {text} \ncleaned_text1: {cleaned_text1}")

# %% noktalama işaretlerini kaldır.
import string

text = "Hello, World! 2025"

cleaned_text2 = text.translate(str.maketrans("" ,"", string.punctuation))

print(f"text: {text} \ncleaned_text2: {cleaned_text2}")

# %% Özel Karakterleri Kaldır %, # , /, &

import re

text = "Hello, #World! 2025%"

cleaned_text3 = re.sub(r"[^A-Za-z0-9\s]", "", text)

print(f"text: {text} \ncleaned_text3: {cleaned_text3}")


# %% Yazim hatalarini düzeltme

from textblob import TextBlob # metin analizlerinde kullanilan kutuphane

text = "Hellıo Wirld! 2025"


cleaned_text4 = TextBlob(text).correct() # correct: yazim hatalarini düzeltir


print(f"text: {text} \ncleaned_text4: {cleaned_text4}")

# %% html yada url etiketlerini kaldir

from bs4 import BeautifulSoup


text = "<div>Hello World! 2025</div>"
# BeatifulSoup ile metni parse et, get_text ile metni çek
cleaned_text5 = BeautifulSoup(text, "html.parser").get_text()

print(f"text: {text} \ncleaned_text5: {cleaned_text5}")
















