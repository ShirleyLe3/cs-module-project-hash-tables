# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

freq = {
    "E": 11.53,
    "T": 9.75,
    "A": 8.46,
    "O": 8.08,
    "H": 7.71,
    "N": 6.73,
    "R": 6.29,
    "I": 5.84,
    "S": 5.56,
    "D": 4.74,
    "L": 3.92,
    "W": 3.08,
    "U": 2.59,
    "G": 2.48,
    "F": 2.42,
    "B": 2.19,
    "M": 2.18,
    "Y": 2.02,
    "C": 1.58,
    "P": 1.08,
    "K": 0.84,
    "V": 0.59,
    "Q": 0.17,
    "J": 0.07,
    "X": 0.07,
    "Z": 0.03,
}

freq = list(freq.items())

def crack(s):
    count = dict()
    cipher = "".join(s.split())
    cipher = s.translate(str.maketrans("", "", ' \'\n":;,.-+=?!1/\\|[]{}()*^&â€”'))
    
    for l in cipher:
        if l not in count:
            count[l] = 1
        count[l] += 1

    count = list(count.items())
    count.sort(key=lambda tup: tup[1], reverse=True)

    decipher = dict()
    for i, tup in enumerate(count):
        decipher[tup[0]] = freq[i][0]

    print(decipher)

    output = ''
    for l in s:
        if l in decipher:
            l = decipher[l]
        output += l

    print(output)


f = open("ciphertext.txt", "r")
crack(f.read())
f.close()