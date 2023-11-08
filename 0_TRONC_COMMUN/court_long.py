# Trouver le mot le plus court et le plus long dans une phrase
# le premier par ordre alphabetique 

# ordre dans la phrase en premier
def get_min_and_max_words(sentense):
    words = sentense.split(" ")
    min_word = min(words, key=len)
    max_word = max(words, key=len)
    return min_word, max_word

# ordre alphabetique en premier

def get_min_and_max_words_sorted2(sentense):
    words = sentense.split(" ")
    words.sort()
    min_word = min(words, key=len)
    max_word = max(words, key=len)
    return min_word, max_word

s = "Un aa sachant chasser sait chasser sans son chien"

min_word, max_word = get_min_and_max_words_sorted2(s)

print("Mot le plus petit:", min_word)
print("Mot le plus long:", max_word)

