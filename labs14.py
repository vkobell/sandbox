#declare the inputs, all three and gather them
input_file = input()
lower_bound = input()
upper_bound = input()

with open(input_file, 'r') as file:#open with "with" to automatically close file once done
    words = [word.strip() for word in file.readlines()]#strip automatically removes whiteline/newline/whitespace

for word in words:
    if lower_bound <= word <= upper_bound:
        print(word)