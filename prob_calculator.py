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
        # select random balls from the hat contents, not allowing for duplicates. If the # of balls being drawn is larger than the contents of the hat, returns the entire self.contents as a list.
        rand_balls = []
        random.seed(95)
        i = 0
        if num_balls >= (len(self.contents) + len(self.not_in_hat)): 
            rand_balls = self.contents
        else:
            while i < num_balls:
                if len(self.contents) == 0: # when the self.contents list is empty, copy the not_in_hat list to it, then empty the not_in_hat list
                    self.contents = self.not_in_hat.copy()
                    self.not_in_hat= [] 
                rand_num = random.randrange(0, len(self.contents))
                rand_balls.append(self.contents[(rand_num - 1)])
                self.not_in_hat.append(self.contents[(rand_num - 1)])
                del self.contents[(rand_num - 1)]
                i += 1
        return rand_balls

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
            except KeyError: # if none of our expected balls where in the results, this is used to avoid an error
                experiment_success = False
                break 
        if experiment_success == True:
            m += 1
    return m/num_experiments
