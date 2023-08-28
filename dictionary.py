import string

def word_frequency(sentence):
    words = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split()
    freq_dict = {}
    
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
    return freq_dict