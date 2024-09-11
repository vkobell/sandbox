#14.9 LAB: Number pattern
#Write a recursive function called print_num_pattern() to output the following number pattern.
#Given a positive integer as input (Ex: 12), subtract another positive integer (Ex: 3) continually until a negative value is reached, and then continually add the second integer until the first integer is again reached.
#For this lab, do not end output with a newline.
#Do not modify the given main program.

#Ex. If the input is:
#12
#3

#the output is:
#12 9 6 3 0 -3 0 3 6 9 12 

#Note: I think the lab is wanting me to subtract the second input from the first input until it gets to 0 and then add the second input to 0 until it reaches the first input again

# TODO: Write recursive print_num_pattern() function

flag = True
numberList = []
total = 0

def print_num_pattern(num1, num2):
    #print(num1, end=' ') #need to print num to start
    global flag 
    global numberList
    global total
    if flag:
        if len(numberList) == 0:
            numberList.append(num1)

        total = num1 - num2
        numberList.append(total)

        if total < 0:
            flag = False

        print_num_pattern(total, num2)

        #flag = True  #sets to true so i can start adding again
    #else
        #print(num1 + num2, end=' ') 
       #sets to true so i can start adding again
    elif not flag:
        total = num1 + num2
        numberList.append(total)

        if (total != numberList[0]):
            print_num_pattern(total, num2)
        #print_num_pattern(num1 + num2, num2, flag) #calling my function so its recursion

        elif (total == numberList[0]):
            my_output = ' '.join(map(str, numberList))
            my_output = my_output.strip()
            print (my_output, end=" ")
            #print(*my_output, sep=" ")
            exit()
   # if flag: # If flag is True, print the number again during the unwind phase
      #  print(num1, end=' ') #where i'll call the num_pattern function -- no commas needed

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)

