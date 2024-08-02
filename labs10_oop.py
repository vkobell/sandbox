# Define your method here
#2,000 steps + 1 mile
#EX: if input is 5345 the output will be 2.67
#EX: if the input is a negative number output will print "Exception: Negative step count entered."

class StepsCalc:
    def __init__(self):
        self.stepscnt = 0
        self.singlestep = .0005
    def steps_to_miles(self, steps):
        return float(steps * self.singlestep)
    
if __name__ == '__main__':
    msg = ""
    stepscalc = StepsCalc()

    try: 
        stepscalc.stepscnt = int(input())

    except: 
        msg = "Your input was not a valid number."

    try:
        if stepscalc.stepscnt > -1:
            miles = stepscalc.steps_to_miles(stepscalc.stepscnt)
            msg = round(miles, 2)
        else:
            raise
    except:
        msg = "Exception: Negative step count entered."

    print (msg)
    #type your code here