# Your code here
def histo(s):
    # normalize whitespace, remove special characters
    s = " ".join(s.split())
    s = s.translate(str.maketrans("", "", '":;,.-+=/\\|[]{}()*^&')).lower().split(" ")
    longest = 0
    count = dict()

    for word in s:
        if word == "":
            pass
        elif word in count:
            count[word] += 1
        else:
            count[word] = 1
        if len(word) > longest:
            longest = len(word)

    count_list = list(count.items())
    count_list.sort(key=lambda tup: (-tup[1], tup[0]))
    
    for tup in count_list:
        spaces = ' ' * (longest - len(tup[0]))
        hashes = '#' * tup[1]
        print(f'{tup[0]}{spaces}{hashes}')

f = open("robin.txt", "r")
histo(f.read())
f.close()