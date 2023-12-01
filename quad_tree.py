
class QuadTree:
    def __init__(self, rectangle: list[float], leaf_size: float, extended_distance: float):

        self.leaves = []
        self.points = []
        self.extended_distance = extended_distance
        self.rectangle = rectangle

        [xmin, xmax, ymin, ymax] = rectangle

        width, height = xmax-xmin, ymax-ymin

        if max(width, height) > leaf_size:
            width /= 2
            height /= 2
            self.leaves.append(QuadTree([xmin, xmax-width, ymin, ymax-height], leaf_size, extended_distance))
            self.leaves.append(QuadTree([xmin+width, xmax, ymin, ymax-height], leaf_size, extended_distance))
            self.leaves.append(QuadTree([xmin, xmax-width, ymin+height, ymax], leaf_size, extended_distance))
            self.leaves.append(QuadTree([xmin+width, xmax, ymin+height, ymax], leaf_size, extended_distance))

    def height(self):
        height = 0
        current = self
        while current.leaves != []:
            current = current.leaves[0]
            height += 1
        return height


    def is_inside_rectangle(self, rectangle, point):
        [xmin, xmax, ymin, ymax] = rectangle
        (x, y) = point

        return xmin <= x and x <= xmax and ymin <= y and y <= ymax


    def insert_point(self, point):
        if self.leaves == []:
            self.points.append(point)
            return

        [xmin, xmax, ymin, ymax] = self.rectangle
        dd = self.extended_distance
        width, height = xmax-xmin, ymax-ymin
        width /= 2
        height /= 2

        if self.is_inside_rectangle([xmin, xmin+width+dd, ymin, ymin+height+dd], point):
            self.leaves[0].insert_point(point)
        if self.is_inside_rectangle([xmin+width-dd, xmax, ymin, ymin+height+dd], point):
            self.leaves[1].insert_point(point)
        if self.is_inside_rectangle([xmin, xmin+width+dd, ymin+height-dd, ymax], point):
            self.leaves[2].insert_point(point)
        if self.is_inside_rectangle([xmin+width-dd, xmax, ymin+height-dd, ymax], point):
            self.leaves[3].insert_point(point)



