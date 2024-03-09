import pytest
import math

from Process.line_warpers import generate_anchor_point_coordinates, rotate


@pytest.mark.parametrize(
    "start_coord,stop_coord,neck_width,neck_height,head_width,head_height,expected_coords",
    [((10, 0), (20, 0), 10, 20, 30, 80, 
     [
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
    ]),
    ((0., 300.), (0., 160.), 170, 90, 400, 550,
[
        (0.0, 330.0),
        (90.0, 330.0),
        (90.0, 400.0),
        (365.0, 400.0),
        (640.0, 400.0),
        (640.0, 90.0),
        (365.0, 90.0),
        (90.0, 90.0),
        (90.0, 160.0),
        (0.0, 160.0),
     ]),
    ],
)
def test_generate_anchor_point_coordinates(start_coord, stop_coord, neck_width, neck_height, head_width, head_height, expected_coords):
    """Test the generate_interlocking_segment function."""
    
    interlocking_segment = generate_anchor_point_coordinates(
        start_coord, stop_coord, neck_width, neck_height, head_width, head_height
    )
    assert interlocking_segment == pytest.approx(expected_coords)


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
