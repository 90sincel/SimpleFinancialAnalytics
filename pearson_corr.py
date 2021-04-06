from math import sqrt
import numpy as np 

returns_general_motors = [0.018, -0.005, -0.047, -0.009, -0.012, 0.003, -0.027, -0.014, 0.029, -0.062, 0.009]
returns_ford = [0.002, -0.004, -0.027, -0.022, -0.001, 0.002, -0.006, -0.017, 0.035, -0.029, 0.002]
returns_exxon_mobil = [0.008, 0.015, 0.009, 0.012, 0.003, -0.007, 0.006, 0.005, -0.048, 0.025, -0.012]
returns_apple = [-0.002, 0.007, -0.004, -0.004, 0.002, 0.013, -0.011, 0.017, -0.001, 0.012, 0.006]

def calculate_correlation(set_x, set_y):
    # sum of all values in each dataset
    sum_x = sum(set_x)
    sum_y = sum(set_y)

    # sum of all squared values in each data set
    sum_x2 = sum([x ** 2 for x in set_x])

    sum_y2 = sum([y ** 2 for y in set_y])
    
    # sum of the product of each respective element in each dataset

    sum_xy = sum([x*y for x,y in zip(set_x,set_y)])
    #sum_xy = 0
    #for x,y in zip(set_x, set_y):
    #    sum_xy += x * y
    print(sum_xy)
    #for i in range(len(set_x)):
    #    sum_xy += set_x[i] * set_y[i]

    # length of dataset
    n = len(set_x)

    # calculate correlation coefficient
    numerator = n * sum_xy - sum_x - sum_y
    denominator = sqrt((n * sum_x2 - (sum_x)**2) * (n * sum_x2 - (sum_y)**2))

    return numerator/denominator


print('The correlation coefficient between General Motors and Ford is', calculate_correlation(returns_general_motors, returns_ford))
print('The correlation coefficient between General Motors and ExxonMobil is', calculate_correlation(returns_general_motors, returns_exxon_mobil))
print('The correlation coefficient between General Motors and Apple is', calculate_correlation(returns_general_motors, returns_apple))

