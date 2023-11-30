
class QuadTree:
    def __init__(self, rectangle: list[float], leaf_size: float):

        self.leaves = []
        self.points = []

        [xmin, xmax, ymin, ymax] = rectangle

        width, height = xmax-xmin, ymax-ymin

        if max(width, height) > leaf_size:
            width /= 2
            height /= 2
            self.leaves.append(QuadTree([xmin, xmax-width, ymin, ymax-height], leaf_size))
            self.leaves.append(QuadTree([xmin+width, xmax, ymin, ymax-height], leaf_size))
            self.leaves.append(QuadTree([xmin, xmax-width, ymin+height, ymax], leaf_size))
            self.leaves.append(QuadTree([xmin+width, xmax, ymin+height, ymax], leaf_size))

    def height(self):
        height = 0
        current = self
        while current.leaves != []:
            current = current.leaves[0]
            height += 1
        return height

