""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    # Write your code below.


    open_fruit_file = open(filename)
    read_fruit_file = open_fruit_file.read()
    return read_fruit_file.split("\n")


def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """

    # Write your code below.

    return list(set(open_and_read).intersection(open_and_read2))
    
    


# Call your functions at the bottom, after they've been defined.

open_and_read = open_and_read_file('fruits_1.txt')
print open_and_read
open_and_read2 = open_and_read_file('fruits_2.txt')
print open_and_read2

comparison = compare(open_and_read, open_and_read2)
print comparison