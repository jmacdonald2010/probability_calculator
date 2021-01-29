import copy
import random

class Hat:

    def __init__(self, **kwargs):
        # init the hat, and create a list for the hat w/ a variable # of kwargs
        self.contents = []
        self.not_in_hat = []
        for key, value in kwargs.items():
            for i in range(0, value):
                self.contents.append(key)

    def draw(self, num_balls): 
        # loop thru random selector given # of times, but don't allow for duplicates, returns list of strings
        rand_balls = []
        # going to change to a while loop so I can keep a sim. logic here
        i = 0
        while i < num_balls:
            if len(self.contents) == 0: # when the self.contents list is empty, copy the not_in_hat list to it, then empty the not_in_hat list
                self.contents = self.not_in_hat.copy()
                self.not_in_hat= [] 
            rand_num = random.randint(0, len(self.contents)) 
            rand_balls.append(self.contents[(rand_num - 1)])
            self.not_in_hat.append(self.contents[(rand_num - 1)])
            del self.contents[(rand_num - 1)]
            i += 1
        # then return all balls to hat
        for ball in self.not_in_hat:
            self.contents.append(ball)
        self.not_in_hat = []
        return rand_balls
            # this may need some addtl work, I'm not sure if the balls in the hat should reset each time the func is called, or if they are out of the hat until the hat is empty

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0 # is # of successful experiments we run
    # first thing is to run the experiment the # of times specified (which is to draw)
    for i in range (0, num_experiments):
        experiment_success = True
        result = hat.draw(num_balls_drawn)
        # then lets clean up the results into a new dict
        org_result = {} # organized results, aka a dict
        # go thru results of the hat.draw, compile those values into a dict
        for ball in result:
            if ball not in org_result:
                org_result[ball] = 1
            else:
                org_result[ball] = org_result[ball] + 1
        # compare results to expected_balls
        # loop thru keys in expected_balls, check to see if vals match w/ those balls in org_result
        for ball in expected_balls: 
            try:
                if org_result[ball] >= expected_balls[ball]:
                    continue
                else:
                    experiment_success = False 
                    break
            except KeyError:
                experiment_success = False
                break 
        if experiment_success == True:
            m += 1
    return m/num_experiments
        





# ex for testing
hat = Hat(black=6, red=4, green=3)
print(hat.draw(5))
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)

# from the actual test itself, b/c for some reason it keeps failing
hat = Hat(red=5,blue=2)
actual = hat.draw(2)
expected = ['blue', 'red']
print("Actual: ", actual, ", Expected: ", expected)

# test from test_module
hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)