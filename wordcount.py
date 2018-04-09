
# def word_count(filename):
#     with open(filename) as f:
#         counts_words = {}
#         for line in f:
#             words = line.split()
#             # print words
#             for word in words:
#                 counts_words[word] = counts_words.get(word, 0) + 1

#         return counts_words

# print word_count("test.txt")








def word_count(filename):
    counts_words = {}
    with open(filename) as f:     
        for line in f:
            words = line.split()
            # print words
            for word in words:
                counts_words[word] = counts_words.get(word, 0) + 1

    return counts_words

def iterating_dict(filename):
    counts_words = word_count(filename)
    for word, count in counts_words.iteritems():
        print word, count
    
iterating_dict("twain.txt")
