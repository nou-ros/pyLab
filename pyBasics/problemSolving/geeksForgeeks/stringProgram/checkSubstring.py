def checkSubstring(sentence, word):
    if(sentence.find(word) == -1):
        print("No")
    else:
        print("Yes")

sentence = "The march of the living"
word = "living"
checkSubstring(sentence, word)
