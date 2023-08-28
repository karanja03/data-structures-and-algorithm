import string

def word_frequency(sentence):
    # Remove punctuation from the sentence and convert to lowercase
    words = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split()
    # Create an empty dictionary to store word frequencies
    freq_dict = {}
    
    # Loop through each word in the list of words
    for word in words:
        # Update the frequency of the current word in the dictionary
        # If the word is not in the dictionary, set its frequency to 1
        # If the word is already in the dictionary, increment its frequency by 1
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
    # Return the dictionary containing word frequencies
    return freq_dict

# Test cases
sentence_1 = "Hello, world! Hello, Python!"
result_1 = word_frequency(sentence_1)
print(result_1)  # Output should be: {'hello': 2, 'world': 1, 'python': 1}

sentence_2 = "The quick brown fox jumps over the lazy dog."
result_2 = word_frequency(sentence_2)
print(result_2)  # Output should be: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

sentence_3 = "To be or not to be, that is the question."
result_3 = word_frequency(sentence_3)
print(result_3)  # Output should be: {'to': 2, 'be': 2, 'or': 1, 'not': 1, 'that': 1, 'is': 1, 'the': 1, 'question': 1}