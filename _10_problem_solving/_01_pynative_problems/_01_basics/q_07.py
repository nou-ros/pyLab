'''
Return the total count of sub-string “Emma” appears in the given string
 “Emma is good developer. Emma is a writer”
'''
#1
sen = "Emma is good developer. Emma is a writer"
n = len(sen)-1
count = sen.count("Emma")
print(count)

#2
def count(sen):
    c=0
    for i in range(len(sen)-1):
    #     c+=sen[i:i+4] == "Emma" another approach
        if sen[i:i+4]=="Emma":
            c+=1
    return c
tot = count(sen)
print("Emma appeared ", tot, "times")
