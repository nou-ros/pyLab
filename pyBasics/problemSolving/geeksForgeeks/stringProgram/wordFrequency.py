def wordFrequency(sentence, word):
    res ={ key: sentence.count(key) for key in sentence.split(' ') }
    print(res) 


sentence = "Nouros is a soon be System Adminintrator. Nouros is a software engineer."
word = "Nouros"
wordFrequency(sentence, word)
