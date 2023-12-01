from geometry import distance

def check_collision(visited, position, width, height, velocity, dt):
    (x, y) = position
    if x < 0 or y < 0 or x > width or y > height:
        return True

    for point in visited:
        if distance(position, point) < velocity * dt + 1e-6:
            return True

    return False

def check_collision_efficient(quad_tree, position, width, height, velocity, dt):
    (x, y) = position
    if x < 0 or y < 0 or x > width or y > height:
        return True

    return quad_tree.check_collision(position, velocity * dt + 1e-6)
