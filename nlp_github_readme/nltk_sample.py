import nltk
string = "I AM A CAT. As yet I have no name."
words_split = nltk.word_tokenize(string)
print(words_split)
words_tag = nltk.pos_tag(words_split)
print(words_tag)