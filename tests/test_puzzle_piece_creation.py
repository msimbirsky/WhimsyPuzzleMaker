import pytest

from Process.line_warpers import generate_anchor_point_coordinates

def test_generate_anchor_point_coordinates():
    """Test the generate_interlocking_segment function."""

    expected_coords = [(10., 0.), (10., 20.), (0., 20.), (0., 60.), (0., 100.), (30., 100.), (30., 60.), (30., 20.), (20., 20.), (20., 0.)]
    start_coord = (10, 0)
    stop_coord = (20, 0)
    neck_width = 10
    neck_height = 20
    head_width = 30
    head_height = 80

    interlocking_segment = generate_anchor_point_coordinates(start_coord, stop_coord, neck_width, neck_height, head_width, head_height)
    assert interlocking_segment == expected_coords