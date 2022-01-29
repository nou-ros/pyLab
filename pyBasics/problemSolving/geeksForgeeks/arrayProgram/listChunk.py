def chunkList(arr, chunkSize):
    for i in range(0, len(arr), chunkSize):
        yield arr[i: i + chunkSize]

def chunkListTwo(arr, chunkSize):
    result = [arr[i : i + chunkSize] for i in range(0, len(arr), chunkSize)]
    return result

size = 5
arr = ["I", "tried", "so", 
        "hard", "in", "the", "end", "it", "doesn't", "even", "matter", "I", "had", "to", "fall", "to", "lose", "it", "all"] 
print(list(chunkList(arr, size)))
print(chunkListTwo(arr, size))
