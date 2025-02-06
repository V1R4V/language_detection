import string
import math
import sys

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


def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X=dict()
    for char in string.ascii_uppercase:
        X[char]=0

    with open (filename, encoding='utf-8') as f:
        for line in f:
            store = line.upper().strip().split(" ")
           # print(store)
            for key in store:
                for char in key:
                    #print(char)
                    if char.isascii():
                        if char.isalpha():
                            if char in X:
                                X[char] += 1

    print("Q1")
    for char in string.ascii_uppercase:
        print(f"{char} {X[char]}")
    return X

def compute_log_probabilities(X, e, s, p_english, p_spanish):
    X1=X['A'] #is this hardcoding fine ??
    e1=e[0]
    s1=s[0]

    if e[0] > 0:
        X1_e1 = X['A'] * math.log(e[0])
    else:
        X1_e1 = 0

    X1_s1 = X['A'] * math.log(s[0]) if s[0] > 0 else 0

    print("Q2")
    print(f"{X1_e1:.4f}")
    print(f"{X1_s1:.4f}")



    F_english= math.log(p_english)
    F_spanish = math.log(p_spanish)

    for i,char in enumerate(string.ascii_uppercase): #crosscheck
        if X[char] > 0:
            F_english += X[char] * math.log(e[i])
            F_spanish += X[char] * math.log(s[i])

    print("Q3")
    print(f"{F_english:.4f}")
    print(f"{F_spanish:.4f}")

    diff = F_spanish - F_english

    if diff >= 100:
        p_english_given_x = 0
    elif diff <= -100:
        p_english_given_x = 1
    else:
        p_english_given_x = 1 / (1 + math.exp(diff))

    print("Q4")
    print(f"{p_english_given_x:.4f}")


def main():
    if len(sys.argv) != 4:
        print("Usage: python3 hw2.py [letter-file] [english-prior] [spanish-prior]")
        sys.exit(1)

    letter_file = sys.argv[1]
    p_english = float(sys.argv[2])
    p_spanish = float(sys.argv[3])

    e, s = get_parameter_vectors()
    X = shred(letter_file)
    compute_log_probabilities(X, e, s, p_english, p_spanish)

if __name__ == "__main__":
    main()