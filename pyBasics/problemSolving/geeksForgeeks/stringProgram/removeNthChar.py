def removeNthChar(sentence, pos):
    newStr = ""
    for i in range(len(sentence)):
        if i != (pos-1):
            newStr = newStr + sentence[i]
    print(newStr)
    

sentence = "Rabindranath Tagore"
removeNthChar(sentence, 5)
