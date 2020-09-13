# coding: utf-8

import random

def main():
    # Takes in file input
    file_input = input("What is the file name? ")
    dict = createDictionary(file_input)
    # Generate 500 word paragraph given input file
    markov_text = generateText(dict, 500)
    print(markov_text)


def createDictionary(filename):
    """
    Accepts a string, which is the name of a text file containing s
    Returns a dictionary whose keys are words encountered in the text f
    """
    pw = '$'

    f = open(filename, encoding = 'latin1')
    text = f.read()
    f.close()

    LoW = text.split()    
    print("There are", len(LoW), "words.")

    d = {}

    for nw in LoW:
        if pw not in d:
            d[pw] = [nw]
        else:
            d[pw] += [nw]

        pw = nw

        # then check for whether that new pw ends in 
        # punctuation -- if it _does_ then set pw = '$'
        if pw[-1] == "!" or pw[-1] == "." or pw[-1] == "?":
            pw = "$"
    return d

def generateText(d, N):
    """
    Takes in a dictionary of word transitions d (generated from createDictionary function)
    Prints a string of n words
    """
    pw = '$'
    for x in range(N):
        nw = random.choice(d[pw])
        print(nw, end= " ")
        #if last character was punctuation 
        if nw[-1] == "!" or nw[-1] == "?" or nw[-1] == ".":
            #then new sentence
            pw = '$'
        #set current word to past word and move on
        else:
            pw = nw

if __name__ == "__main__":
    main()
            
