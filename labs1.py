import statistics


#Uinput = input().split() #written first to turn input into list//version without verbosity and zero split specific char
Uinput = input('Please enter your input(s) and seperate with comma if needed: ').split(',') #written first to turn input into list//version WITH verbosity and char specific split function

my_list = []

for num in Uinput:
     my_list.append(int(num))
    
list_avg = statistics.mean(my_list)
my_list.sort(reverse = True)

print(list_avg, my_list[0])
