14.8 LAB: All permutations of names
Write a program that lists all ways people can line up for a photo (all permutations of a list of strings). The program will read a list of one word names, then use a recursive function to create and output all possible orderings of those names separated by a comma, one ordering per line.

When the input is:

Julia Lucas Mia
then the output is (must match the below ordering):

Julia, Lucas, Mia 
Julia, Mia, Lucas
Lucas, Julia, Mia
Lucas, Mia, Julia
Mia, Julia, Lucas
Mia, Lucas, Julia
428214.2256588.qx3zqy7


def print_all_permutations(permList, nameList):
    # TODO: Implement method to create and output all permutations of the list of names.

if __name__ == "__main__": 
    nameList = input().split(' ')
    permList = []
    print_all_permutations(permList, nameList)