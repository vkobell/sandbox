#This is for the fat burning heart rate lab
def get_age():
    age = int(input()) #input added to get age
    if age < 18 or age > 75: #conditions added
        raise ValueError('Invalid age.') #todo: Raise exception for invalid ages
    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = 0.7 * (220 - age) #added calc
    return heart_rate

if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a', age, 'year-old:', 
              f'{heart_rate:.1f} bpm')
    except ValueError as e:
        print(e)
        print('Could not calculate heart rate info.')