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


def compute_log_probabilities(X, e, s, p_english, p_spanish):
    X1=X['A']
    e1=e[0]
    s1=s[0]

    if e[0] > 0:
        X1_e1 = X[0] * math.log(e[0])
    else:
        X1_e1 = 0

    X1_s1 = X[0] * math.log(s[0]) if s[0] > 0 else 0

    print("Q2")
    print(f"{X1_e1:.4f}")
    print(f"{X1_s1:.4f}")


    F_english= math.log(p_english)
    F_spanish = math.log(p_spanish)

    for i,char in string.ascii_uppercase:
        if X[char] > 0:
            F_english += X[char] * math.log(e[i])
            F_spanish += X[char] * math.log(s[i])

    print("Q3")
    print(f"{F_english:.4f}")
    print(f"{F_spanish:.4f}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 hw2.py [letter-file] [english-prior] [spanish-prior]")
        sys.exit(1)

    letter_file = sys.argv[1]
    p_english = float(sys.argv[2])
    p_spanish = float(sys.argv[3])

    # Get parameters
    e, s = get_parameter_vectors()

    # Get character counts and print Q1
    X = shred(letter_file)

    # Compute and print probabilities for Q2-Q4
    compute_log_probabilities(X, e, s, p_english, p_spanish)


if __name__ == "__main__":
    main()