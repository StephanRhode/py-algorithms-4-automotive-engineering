from pytest import approx
import math

from my_source import euclid


def test_euclid():
    a = [0, 0, 0]
    b = [4, 4, 4]
    dist = euclid(a, b)
    assert(math.sqrt(48.) == approx(dist))