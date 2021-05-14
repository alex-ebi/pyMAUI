from shootingpidemo.utils import Random2dPoint


def test_2d_point_attributes():
    point = Random2dPoint()
    assert hasattr(point, 'x')
    assert hasattr(point, 'y')


def test_overwriting_2d_point_attributes():
    point = Random2dPoint()
    point.x, point.y = [0., 1.]


def test_picking_2d_point():
    point = Random2dPoint()
    overwrite_value = 42
    point.x, point.y = [overwrite_value, overwrite_value]
    point.pick_random_point()
    assert point.x != overwrite_value
    assert point.y != overwrite_value
