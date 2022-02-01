def palindrome(word):
    mid = (len(word) - 1)//2
    for i in range(0, mid):
        if word[i] != word[len(word)-i-1]:
            return False
        return True

def palindromeTwo(word):
    return True if ''.join(reversed(word)) == word else False


def palindromeThree(word):
    return word == word[::-1]

word = "malayalam"
print(palindrome(word))
print(palindromeTwo(word))
print(palindromeThree(word))
