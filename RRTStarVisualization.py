import cv2

img_size = 500
img = np.zeros((img_size, img_size, 3), dtype='np.uint8')

# Draw nodes and edges
for node in nodes:
    if node.parent:
        cv2.line(img, (int(node.x * 50), int(node.y * 50)), (int(node.parent.x * 50), int(node.parent.y * 50)), (255, 255, 255), 1)
    cv2.circle(img, (int(node.x * 50), int(node.y * 50)), 2, (0, 0, 255), -1)

# Draw start and goal
cv2.circle(img, (int(start_node.x * 50), int(start_node.y * 50)), 5, (0, 255, 0), -1)
cv2.circle(img, (int(goal_node.x * 50), int(goal_node.y * 50)), 5, (0, 255, 0), -1)

# Draw obstacles
for obstacle in obstacles:
    cv2.circle(img, (int(obstacle.x * 50), int(obstacle.y * 50)), int(obstacle.radius * 50), (255, 255, 255), -1)

cv2.imshow('RRT* Visualization', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
