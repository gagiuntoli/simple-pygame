from quad_tree import QuadTree

def test_check_height():

    quad_tree = QuadTree([0,1,0,1], 1.1)
    assert quad_tree.height() == 0

    quad_tree = QuadTree([0,1,0,1], 0.9)
    assert quad_tree.height() == 1

    quad_tree = QuadTree([0,1,0,1], 0.49)
    assert quad_tree.height() == 2

    quad_tree = QuadTree([0,1,0,1], 0.24)
    assert quad_tree.height() == 3

    quad_tree = QuadTree([0,1,0,1], 0.12)
    assert quad_tree.height() == 4

