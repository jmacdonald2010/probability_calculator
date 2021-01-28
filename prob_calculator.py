import copy
import random

class Hat:

    def __init__(self, **kwargs):
        # init the hat, and create a list for the hat w/ a variable # of kwargs
        self.contents = []
        for key, value in kwargs.items():
            for i in range(0, value):
                self.contents.append(key)

    def draw(self, num_balls): # need to update something here; needs to reduce contents in contents
        # loop thru random selector given # of times, but don't allow for duplicates, returns list of strings
        nums_used = []
        rand_balls = []
        # going to change to a while loop so I can keep a sim. logic here
        i = 0
        while i < num_balls:
            rand_num = random.randint(0, (len(self.contents) - 1)) # not sure about this, randint may be including the second #
            if rand_num in nums_used:
                continue
            nums_used.append(rand_num)
            rand_balls.append(self.contents[rand_num])
            i += 1
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