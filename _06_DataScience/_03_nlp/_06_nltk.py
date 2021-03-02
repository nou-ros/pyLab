import string 
from collections import Counter
import matplotlib.pyplot as plt

#tokenizer
from nltk.tokenize import word_tokenize

#stop words
from nltk.corpus import stopwords

# sentiment
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = open('_01_test.txt', encoding='utf-8').read()
lower_text = text.lower()
cleaned_text = lower_text.translate(str.maketrans("","",string.punctuation))

# using nltk tokenization which is much faster for large data
tokenized_words = word_tokenize(cleaned_text, "english")

final_words=[]
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

emotion_list = []
count = 0
with open('_03_emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(":")
        if word in final_words:
            count+=1
            emotion_list.append(emotion)

count = Counter(emotion_list)

# sentiment analysis
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    # print(score)
    neg = score['neg']
    pos = score['pos']

    if neg > pos:
        print("Negative sentiment")
    elif pos > neg:
        print('Positive sentiment')
    else:
        print("Neutral")

sentiment_analyse(cleaned_text)

'''
matplotlib functions
'''
fig, ax1 = plt.subplots()
ax1.bar(count.keys(), count.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()