import pytest
import math

from Process.line_warpers import generate_anchor_point_coordinates, rotate


def test_generate_anchor_point_coordinates():
    """Test the generate_interlocking_segment function."""

    expected_coords = [(10., 0.), (10., 20.), (0., 20.), (0., 60.), (0., 100.), (30., 100.), (30., 60.), (30., 20.), (20., 20.), (20., 0.)]
    
    expected_coords = [
        (10.0, 0.0),
        (10.0, 20.0),
        (0.0, 20.0),
        (0.0, 60.0),
        (0.0, 100.0),
        (30.0, 100.0),
        (30.0, 60.0),
        (30.0, 20.0),
        (20.0, 20.0),
        (20.0, 0.0),
    ]
    start_coord = (10, 0)
    stop_coord = (20, 0)
    neck_width = 10
    neck_height = 20
    head_width = 30
    head_height = 80

    interlocking_segment = generate_anchor_point_coordinates(
        start_coord, stop_coord, neck_width, neck_height, head_width, head_height
    )
    assert interlocking_segment == expected_coords


def test_rotate_90_degrees():
    """Test case 1: Rotate 90 degrees."""
    origin = (0, 0)
    point = (3, 4)
    angle = math.radians(90)
    expected_point = (-4, 3)
    assert rotate(origin, point, angle) == pytest.approx(expected_point)


def test_rotate_180_degrees():
    """Test case 2: Rotate 180 degrees."""
    origin = (0, 0)
    point = (1, 1)
    angle = math.radians(180)
    expected_point = (-1, -1)
    assert rotate(origin, point, angle) == pytest.approx(expected_point)


def test_rotate_neg_45_degrees():
    """Test case 3: Rotate -45 degrees."""
    origin = (0, 0)
    point = (1, 1)
    angle = math.radians(-45)
    expected_x = math.sqrt(2)
    expected_y = 0
    rotated_point = rotate(origin, point, angle)
    assert rotated_point[0] == pytest.approx(expected_x)
    assert rotated_point[1] == pytest.approx(expected_y)
