integerInput = [int(x) for x in input('Input a list of integers seperated with a singular space').split()]
rangeInput = [int(x) for x in input('Input two numbers for a low to high range seperated with a singular space').split()]

#integerInput = [int(x) for x in input().split()] //integer without verbosity or char specifics
#rangeInput = [int(x) for x in input().split()] //range without verbosity or char specifics


#for loop in conditions int:
for number in integerInput:
    if rangeInput[0] <= number <= rangeInput[1]:
        print('{}'.format(number), end = ' ')



