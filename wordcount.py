# put your code here.
def word_count(filename):
    with open(filename) as f:
        counts_words = {}
        for line in f:
            words = line.split()
            # print words
            for word in words:
                counts_words[word] = counts_words.get(word, 0) + 1

        return counts_words

print word_count("test.txt")
