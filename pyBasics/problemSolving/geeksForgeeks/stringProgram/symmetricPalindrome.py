def symmetricalPalindrome(word):
    mid = (len(word)-1)//2
    start = 0
    tempStart = start
    last = len(word) - 1
    tempLast = last
    flag = 0
    flag1 = 0
    # palindrome check
    while(tempStart <= mid):
        if(word[tempStart] == word[tempLast]):
            tempStart += 1
            tempLast -= 1
        else:
            flag = 1
            break;

    tempMid = mid + 1
    # symmetrical check
    while(start <= mid and tempMid <= last):
        if(word[start] == word[tempMid]):
            start += 1
            tempMid += 1
        else:
            flag1 = 1
            break;
    if(flag == 0 and flag1 == 0):
        print("word is both symmetrical and palindrome")
    elif(flag == 0 and flag1 == 1):
        print("word is not symmetrical but palindrome")
    elif(flag == 1 and flag1 == 0):
        print("word is not palindrome but symmetrical")
    else:
        print("word is not symmetrical nor palindrome")

word = "amaama"
word2 = "khokho"
symmetricalPalindrome(word2)
