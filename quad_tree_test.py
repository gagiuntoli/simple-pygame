from quad_tree import QuadTree

def test_check_height():

    dist = 0.0
    quad_tree = QuadTree([0,1,0,1], 1.1, dist)
    assert quad_tree.height() == 0

    quad_tree = QuadTree([0,1,0,1], 0.9, dist)
    assert quad_tree.height() == 1

    quad_tree = QuadTree([0,1,0,1], 0.49, dist)
    assert quad_tree.height() == 2

    quad_tree = QuadTree([0,1,0,1], 0.24, dist)
    assert quad_tree.height() == 3

    quad_tree = QuadTree([0,1,0,1], 0.12, dist)
    assert quad_tree.height() == 4


def test_insert_point():
    dist = 0.1
    quad_tree = QuadTree([0,1,0,1], 0.9, dist)
    quad_tree.insert_point((0.25, 0.25))
    assert quad_tree.leaves[0].points == [(0.25, 0.25)]
    assert quad_tree.leaves[1].points == []
    assert quad_tree.leaves[2].points == []
    assert quad_tree.leaves[3].points == []

    dist = 0.1
    quad_tree = QuadTree([0,1,0,1], 0.9, dist)
    quad_tree.insert_point((0.45, 0.45))
    assert quad_tree.leaves[0].points == [(0.45, 0.45)]
    assert quad_tree.leaves[1].points == [(0.45, 0.45)]
    assert quad_tree.leaves[2].points == [(0.45, 0.45)]
    assert quad_tree.leaves[3].points == [(0.45, 0.45)]

    dist = 0.0
    quad_tree = QuadTree([0,1,0,1], 0.9, 0.0)
    quad_tree.insert_point((0.45, 0.45))
    assert quad_tree.leaves[0].points == [(0.45, 0.45)]
    assert quad_tree.leaves[1].points == []
    assert quad_tree.leaves[2].points == []
    assert quad_tree.leaves[3].points == []

    dist = 0.1
    quad_tree = QuadTree([0,1,0,1], 0.9, dist)
    point = (0.55, 0.55)
    quad_tree.insert_point(point)
    assert quad_tree.leaves[0].points == [point]
    assert quad_tree.leaves[1].points == [point]
    assert quad_tree.leaves[2].points == [point]
    assert quad_tree.leaves[3].points == [point]

    dist = 0.1
    quad_tree = QuadTree([0,1,0,1], 0.9, dist)
    point = (0.45, 0.55)
    quad_tree.insert_point(point)
    assert quad_tree.leaves[0].points == [point]
    assert quad_tree.leaves[1].points == [point]
    assert quad_tree.leaves[2].points == [point]
    assert quad_tree.leaves[3].points == [point]

    dist = 0.1
    quad_tree = QuadTree([0,1,0,1], 0.9, dist)
    point = (0.55, 0.45)
    quad_tree.insert_point(point)
    assert quad_tree.leaves[0].points == [point]
    assert quad_tree.leaves[1].points == [point]
    assert quad_tree.leaves[2].points == [point]
    assert quad_tree.leaves[3].points == [point]

    dist = 0.1
    quad_tree = QuadTree([0,1,0,1], 0.9, dist)
    p1 = (0.55, 0.45)
    p2 = (0.25, 0.25)
    quad_tree.insert_point(p1)
    quad_tree.insert_point(p2)
    assert quad_tree.leaves[0].points == [p1, p2]
    assert quad_tree.leaves[1].points == [p1]
    assert quad_tree.leaves[2].points == [p1]
    assert quad_tree.leaves[3].points == [p1]

