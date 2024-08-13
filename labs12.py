import random #ODO: Import the random module

def number_guess(num):     #Get a random number between 1-100
    random_number = random.randint(1, 100)
    
    if num < random_number:     #Compare parameter num to the random number
        print(f"{num} is too low. Random number was {random_number}.")
    elif num > random_number:
        print(f"{num} is too high. Random number was {random_number}.")
    else:
        print(f"{num} is correct!")

if __name__ == "__main__":     #Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)
    user_input = input()
    tokens = user_input.split()

    for token in tokens:         # Convert the string tokens into integers
        num = int(token)
        number_guess(num)