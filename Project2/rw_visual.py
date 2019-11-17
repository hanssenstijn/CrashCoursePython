import matplotlib.pyplot as plt

from random_walk import RandomWalk

# make a random walk, and plot the points
rw = RandomWalk()
rw.fill_walk()
# color the points so we can follow the path it took
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
edgecolor='none', s=15)
# Emphasize the first and last points.
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
s=100)

plt.show()