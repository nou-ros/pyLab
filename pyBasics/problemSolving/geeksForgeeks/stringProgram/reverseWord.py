def reverseSentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    print(reverse_sentence)

sentence = "Asian kung fu generation"
reverseSentence(sentence)
