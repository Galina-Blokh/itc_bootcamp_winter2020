'''
Exercise - What is wrong?
Run the following code. Try to understand the error that you are getting.
1. What part of the error would you search in google?

IndexError: boolean index did not match indexed array along dimension 0;
dimension is 4 but corresponding boolean dimension is 5

2. Fix the error according to what you find.
Submit what you looked for online, as well as the revised code.
'''

import numpy as np
def subtract_smooth(x, y):
 y_new = y - median_filter(x, y, 1.)
 return y_new

def median_filter(x, y, width):
 y_new = np.zeros(y.shape)
 for i in range(len(x)):
  y_new[i] = np.median(y[np.abs(x - x[i]) < width * 0.5])
 return y_new

subtract_smooth(np.array([1,2,3,4,5][1:]),np.array([4,5,6,8]))
# using an incorrect arr lenth -> should be the same size