#14.8 LAB: All permutations of names
#Write a program that lists all ways people can line up for a photo (all permutations of a list of strings). The program will read a list of one word names, then use a recursive function to create and output all possible orderings of those names separated by a comma, one ordering per line.

#When the input is:

#Julia Lucas Mia
#then the output is (must match the below ordering):

#Julia, Lucas, Mia 
#Julia, Mia, Lucas
#Lucas, Julia, Mia
#Lucas, Mia, Julia
#Mia, Julia, Lucas
#Mia, Lucas, Julia


def print_all_permutations(permList, nameList):
    if not nameList:  #--> not operator will take a true/false value and flips it
        print(", ".join(permList))  #join will combine variables from a list 
        return

    for i in range(len(nameList)):
        current_name = nameList[i]  
        remaining_names = nameList[:i] + nameList[i+1:]  
        print_all_permutations(permList + [current_name], remaining_names) #-->this is the part where its recursive because its calling itself

if __name__ == "__main__": 
    nameList = input().split(' ')
    permList = [] #-->declares list
    print_all_permutations(permList, nameList) 