# a python program to identify people using a dna
"""https://stackoverflow.com/questions/61131768/how-to-count-consecutive-substring-in-a-string-in-python-3"""

import csv
import sys


def main():

    # check for command line argument
    if len(sys.argv) != 3:
        print("missing command-line argument")
        sys.exit(1)

    # a list of the csvfile
    database = []
    # open the csv file
    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            database.append(row)

    text = open_txtfile()
    genes = get_gene()
    # a list of the result from search_txtfile function
    num = []

    # on every iteration of genes, take a gene and search&count the textfile for the maximum consective repetition
    for k in range(len(genes)):
        count = search_txtfile(text, genes[k])
        num.append(count)
        
    # compare function is called
    compare(database[1:], num)

# open the textfile
def open_txtfile():
    dnasequence = open(sys.argv[2])
    text = dnasequence.read()
    dnasequence.close()
    return text


# function to get the genes i.e AATG, AGATC as the case may be
def get_gene():
    with open(sys.argv[1], 'r') as f:
        reader = csv.reader(f)
        genes = next(reader)
        genes.remove('name')
    return genes

# function to search and count the dna sequence of a textfile for maximum consective repeats
def search_txtfile(text, genes):
    count = 0
    value_length = len(genes)
    text_length = len(text)
    for k in range(round((text_length / value_length))):
        if (k * genes) in text:
            count = k
    return count
    

# a list of the dna figures that is meant to be cross-checked with num
verify = []
# a function to compare the database and textfile.
def compare(database, num):
    '''this function iterates through a nested database list.
       on each iteration of the nested list it clears verify, omittes the first element of that list and finds the length of the x.
       on each iteration of the nested loop, it converts the dna figures of the individuals to integer and appends it to verify'''
    for lst in database:
        verify.clear()
        x = lst[1:]
        length = len(x)
        for nest_list in x:
            int_seq = int(nest_list)
            verify.append(int_seq)
        # check if the nested loop is done iterating
        if length == length:
            # check if list num isn't exactly the same with verify list.
            if num != verify:
                continue
            else:
                # print the name of the person whose dna has been identified
                print(lst[0])
                break
    # if after all the iterating through the above loopes, num is certainly num != verify, print no match
    if num != verify:
        print("No match")
        
main()
