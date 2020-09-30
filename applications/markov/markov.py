import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()


def markov_words(s):
    words = dict()
    s = s.replace("\n", " ")
    s = s.split(" ")

    for i, word in enumerate(s):
        if word != "":
            if i + 1 < len(s):
                if word not in words:
                    words[word] = []
                if s[i + 1] != "":
                    words[word].append(s[i + 1])

    words = list(words.items())
    return words


def markov_sentence(d, rounds=1):
    if rounds < 1:
        rounds = 1
    for i in range(rounds):
        output = ""

        while True:
            # choose a start word
            word = random.choice(d)
            while word[0][-1] in '.!?"':
                word = random.choice(d)
            word1 = word[0]
            # choose a next word
            word2 = random.choice(word[1])
            output += f"{word1} {word2} "
            # if there's punctuation at the end, break loop
            if word2 != "" and word2[-1] in '.!?"':
                break

        output = output.strip()
        print(output, end="\n\n")


mw = markov_words(words)
markov_sentence(mw, 5)