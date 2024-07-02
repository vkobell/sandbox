import numpy as np

#userInput = input().split() #written first to turn input into list//version without verbosity and zero split specific char
userInput = input('Please enter your input(s) and seperate with comma if needed: ').split(',') #written first to turn input into list//version WITH verbosity and char specific split function
my_list = []

for num in userInput:  
     if int(num)>=0:
           my_list.append(int(num))

my_list.sort() 
mystring = ' '.join(map(str, my_list)) #turned list into string

print(mystring, end=" ") #fixed end spacing 