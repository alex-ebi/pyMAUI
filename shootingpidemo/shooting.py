import numpy as np

from shootingpidemo.utils import Random2dPoint


def hits_circle(point: Random2dPoint) -> bool:
    """
    Check if point hits circle with radius 1.

    Parameters
    ----------
    point : Random2dPoint
        Point with random x-/y-value between 0 and 1.

    Returns
    -------
    hit_status : bool
    """
    if not isinstance(point, Random2dPoint):
        raise ValueError("Point is not a Random2dPoint object")
    vector_length = np.sqrt(point.x**2 + point.y**2)
    if vector_length <= 1:
        return True
    return False
