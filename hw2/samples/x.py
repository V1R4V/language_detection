import string

X = dict()
for char in string.ascii_uppercase:
    X[char] = 0

with open('letter3.txt', encoding='utf-8') as f:
    for line in f:
        store = line.upper().strip().split(" ")
        for key in store:
            for char in key:
                if char.isascii():
                    if char.isalpha():
                        if char in X:
                            X[char] += 1
                        else:
                            X[char] = 1

print(X)


