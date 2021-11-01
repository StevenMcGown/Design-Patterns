from google.cloud import translate_v2 as translate

import UpdateSheet
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="creds/translate.json"

translate_client = translate.Client()

data = open("words.txt")
data = data.readlines()

words = list()

for line in data:
    word = line.split("\t", 1)[0]
    print("Translating " + word + "...")
    translatedWord = translate_client.translate(word, target_language='en')
    data = (word, translatedWord["translatedText"],"","black")
    words.append(data)

UpdateSheet.updateSpreadsheet(words)