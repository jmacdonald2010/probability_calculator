# probability_calculator
Completed in part for freeCodeCamp's Scientific Computing with Python course.

This project presents a probability calculator. The project simulates balls of different colors placed into a hat as a class. The hat class has a draw method, which draws balls from the hat at random, and replacing them all when it runs out. However, if the number of balls drawn is larger than the contents of the hat, the draw method returns the list of the hat contents instead.

This project also contains an experiment function, which takes a hat object, a dictionary containing the expected results, the number of balls to draw, and how many times the experiment should be run. The function returns a probability as the number of successful experiments divided by the number of experiments run.
