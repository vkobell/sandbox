# Define your method here
#2,000 steps + 1 mile
#EX: if input is 5345 the output will be 2.67
#EX: if the input is a negative number output will print "Exception: Negative step count entered."

#class StepsCalc:
    #def __init__(self):
        #self.stepscnt = 0
        #self.singlestep = .0005
def steps_to_miles(steps):
        singlestep = .0005
       # try:
        if steps > 0:
            return float(steps * singlestep)
        else:
            raise ValueError("Exception: Negative step count entered.")
      #  except ValueError as e:
           # print(e)
            #print("Exception: Negative step count entered.")


    
if __name__ == '__main__':
    msg = ""
    #stepscalc = StepsCalc()
    stepscnt = 0
    try: 
        stepscnt = int(input())

    except: 
        print("Your input was not a valid number.")

    try:
        if stepscnt < 0:
            raise 
        else:
            miles = steps_to_miles(stepscnt)
            if miles:
                msg = round(miles, 2)
                print (msg)
    except:
        print("Exception: Negative step count entered.")

        #else:
            #raise
    #except:
       # msg = "Exception: Negative step count entered."

    #print (msg)
    #type your code here