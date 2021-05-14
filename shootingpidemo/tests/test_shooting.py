import pytest

from shootingpidemo.shooting import hits_circle
from shootingpidemo.utils import Random2dPoint


def test_hit():
    point = Random2dPoint()

    point.x, point.y = [0., 0.]
    assert hits_circle(point)

    point.x, point.y = [1., 0.]
    assert hits_circle(point)

    point.x, point.y = [0., 1.]
    assert hits_circle(point)


def test_miss():
    point = Random2dPoint()

    point.x, point.y = [1., 1.]
    assert not hits_circle(point)

    point.x, point.y = [42., 0.]
    assert not hits_circle(point)


def test_non_valid_point():
    with pytest.raises(ValueError):
        hits_circle([0., 0.])
