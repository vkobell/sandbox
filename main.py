import statistics

Uinput = input('Please enter your input(s): ').split() #written first to turn input into list
my_list = []

for num in Uinput:
     my_list.append(int(num))
    
#list_avg = int
list_avg = statistics.mean(my_list)
my_list.sort(reverse = True)

print(list_avg, my_list[0])
