import copy
import random

class Hat:

    def __init__(self, **kwargs):
        # init the hat, and create a list for the hat w/ a variable # of kwargs
        self.contents = []
        for key, value in kwargs.items():
            for i in range(0, value):
                self.contents.append(key)

    def draw(self, num_balls):
        # loop thru random selector given # of times, but don't allow for duplicates, returns list of strings
        nums_used = []
        rand_balls = []
        for i in range(0, num_balls):
            rand_num = random.randint(0, len(self.contents))
            if rand_num in nums_used:
                continue
            nums_used.append(rand_num)
            rand_balls.append(self.contents[rand_num])
            # this may need some addtl work, I'm not sure if the balls in the hat should reset each time the func is called, or if they are out of the hat until the hat is empty

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass # until i write the actual function





# ex for testing
hat = Hat(black=6, red=4, green=3)
# commented out until i write this func
'''probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)'''