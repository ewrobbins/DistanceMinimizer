# Eric Robbins
# A quick test of scipy's solution to the assignment (cost-matrix) problem

import random
import numpy as np
from scipy.optimize import linear_sum_assignment
import math

X_RANGE = 100
Y_RANGE = 100

# randomize stations and centroids (workers and jobs, respectively, in the classic assignment problem)
# format is (index, x_coord, y_coord)
stations = [(i, random.randint(-X_RANGE, X_RANGE), random.randint(-Y_RANGE, Y_RANGE)) for i in range(15)]
centroids = [(i, random.randint(-X_RANGE, X_RANGE), random.randint(-Y_RANGE, Y_RANGE)) for i in range(15)]

# calculate pythagorean distance between two xy coords
def pyth_dist(pt1, pt2):

    return math.sqrt(math.pow((pt2[1] - pt1[1]), 2) + math.pow((pt2[2] - pt1[2]), 2))


# create empty numpy array
m = len(stations)
n = len(centroids)
cost_mat = np.empty(shape=(m,n))

newRow = []
temp_arr = []

# make matrix out of station->centroid distances
for j in range(n):
    for i in range(m):
        newRow.append(pyth_dist(stations[i], centroids[j]))
    temp_arr.append(newRow)
    newRow = []

# fill numpy array
cost_mat = np.array(temp_arr)

# find optimized pairings (hungarian method)
opt_row, opt_col = linear_sum_assignment(cost_mat)


# output ordered pairs
print_list = []
for i in range(len(opt_row)):
    print_list.append((stations[opt_row[i]], centroids[opt_col[i]]))

print(print_list)
