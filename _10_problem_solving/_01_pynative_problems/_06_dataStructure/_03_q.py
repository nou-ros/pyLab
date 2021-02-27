'''
Given a list slice it into a 3 equal chunks and reverse each list
'''
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]

length = len(sampleList)
chunk = length//3

start = 0
end = chunk

for i in range(1, 4):
    listChunk = sampleList[start:end:1]
    print("Chunk ", i, listChunk)
    print("After reverse: ", listChunk[::-1])
    start = end
    end +=chunk

