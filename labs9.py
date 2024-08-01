#Given a list of 10 names, complete the program that outputs the name specified by the list index entered by the user.
#Use a try block to output the name and an except block to catch any IndexError.
#Output the message from the exception object if an IndexError is caught.
#Output the first element in the list if the invalid index is negative or the last element if the invalid index is positive.
names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())
msg = ""

try:
    if index >= 0 and index < len(names):
        msg = "Name: " + names[index]
    else:
        raise 

except:
    #msg = "You hit the except"
    if index > len(names) - 1:
        msg = "Exception! list index out of range\nThe closest name is: " + names[9]
    elif index < 0 and index >- len(names):
        msg = "Name: " + names[len(names) + index]
    elif index < -9:
       msg = "Exception! list index out of range\nThe closest name is: " + names[0]

print(msg)


