def reverse_words(sentence):
    words = sentence.split()
    reversed_sentece = " ".join(reversed(words))
    return reversed_sentece

sentence = "R a c e c a R"
reversed_sentece = reverse_words(sentence)
print("reversed_sentence:", reversed_sentece)