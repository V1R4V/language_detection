import string
def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)


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

    print("Q1")
    for char in string.ascii_uppercase:
        print(f"{char} {X[char]}")


