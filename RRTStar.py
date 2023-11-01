import random
import math
import numpy as np

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

def euclidean_distance(node1, node2):
    return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)

def rrt_star(start, goal, obstacles, max_iter, step_size):
    nodes = [start]
    for _ in range(max_iter):
        rand_node = Node(random.uniform(0, 10), random.uniform(0, 10))  # Adjust the bounds as needed.
        nearest_node = min(nodes, key=lambda node: euclidean_distance(node, rand_node))
        new_node = Node(nearest_node.x + step_size, nearest_node.y + step_size)  # Adjust step size.

        if not any(obstacle.collides(new_node) for obstacle in obstacles):
            new_node.parent = nearest_node
            nodes.append(new_node)

    return nodes

class Obstacle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def collides(self, node):
        return euclidean_distance(Node(self.x, self.y), node) < self.radius

start_node = Node(1, 1)
goal_node = Node(9, 9)
obstacles = [Obstacle(4, 4, 1), Obstacle(7, 7, 1)]  # Define obstacles as needed.

max_iter = 1000
step_size = 0.1

nodes = rrt_star(start_node, goal_node, obstacles, max_iter, step_size)
 