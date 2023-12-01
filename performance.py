from quad_tree import QuadTree
from time import time
from random import random 
from collision import check_collision, check_collision_efficient

WIDTH = 1000
HEIGHT = 1000
MAX_POINTS = 10000

VELOCITY = 10.0
DT = 1.0

points = []
for i in range(MAX_POINTS):
    points.append((random()*WIDTH, random()*HEIGHT))

visited = []
quad_tree = QuadTree([0, WIDTH, 0, HEIGHT], VELOCITY * DT * 20, VELOCITY * DT + 1e-6)

start = time()
for point in points:
    visited.append(point)
print("time insert (naive)", time() - start)

start = time()
for point in points:
    quad_tree.insert_point(point)
print("time insert (quad_tree)", time() - start)

points = []
for i in range(MAX_POINTS):
    point = (random()*WIDTH, random()*HEIGHT)
    points.append(point)
    assert check_collision(visited, point, WIDTH, HEIGHT, VELOCITY, DT) == check_collision_efficient(quad_tree, point, WIDTH, HEIGHT, VELOCITY, DT)

start = time()
for point in points:
    check_collision(visited, point, WIDTH, HEIGHT, VELOCITY, DT)
print("time check collision (naive)", time() - start)

start = time()
for point in points:
    check_collision_efficient(quad_tree, point, WIDTH, HEIGHT, VELOCITY, DT)
print("time check collision (quad_tree)", time() - start)
