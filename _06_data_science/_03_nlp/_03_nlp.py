import string 
text = open('_01_test.txt', encoding='utf-8').read()
lower_text = text.lower()
cleaned_text = lower_text.translate(str.maketrans("","",string.punctuation))
tokenized_words = cleaned_text.split()
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

final_words=[]
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

'''
NLP Emotion algorithms
1. Check if the word in the final word list is also present in emotion.txt
- open the emotion file
- loop through each line and clear it
- extract the word and emotion using split

2. If word is present in text file -> Add the emotion to emotion_list
3. Finally count each emotion in the emotion list using Counter
'''
emotion_list = []
count = 0
with open('_03_emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(',','').replace("'",'').strip()
        # print(clear_line)
        word, emotion = clear_line.split(":")
        # print("word: " + word + ", " + "emotion:" + emotion)
        if word in final_words:
            count+=1
            emotion_list.append(emotion)

print(emotion_list, count)

from collections import Counter
count = Counter(emotion_list)
print(count)