from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# example_string = """
# Muad'Dib learned rapidly because his first training was in how to learn.
# And the first lesson of all was the basic trust that he could learn.
# It's shocking to find how many people do not believe they can learn,
# and how many more believe learning to be difficult."""

# print(sent_tokenize(example_string))
# print(word_tokenize(example_string))

worf_quote = "Sir, I protest. I am not a merry man!"
words_in_quote = word_tokenize(worf_quote)
print(words_in_quote)
stop_words = set(stopwords.words("english"))
filtered_list = []

for word in words_in_quote:
    if word.casefold() not in stop_words:
        filtered_list.append(word)
print(filtered_list)