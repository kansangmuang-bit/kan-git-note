from functools import reduce

a_list = [50, 30, 10, 20]

def multiply(a, b):
    print(f"{a=}, {b=}")
    return a * b


result = reduce(multiply, a_list)
print(result)


def manipulate_words(word1, word2):
    print(word1, word2)
    if len(word1) < len(word2):
        return word1 
    else:
        return word1 + word2
    
words = ["hi", "fire", "I", "apple", "cat"]

result = reduce(manipulate_words, words)
print(result)