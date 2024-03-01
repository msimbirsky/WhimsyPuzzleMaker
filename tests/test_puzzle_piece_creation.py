import pytest

from Process.line_warpers import generate_interlocking_segment

def test_generate_interlocking_segment():
    """Test the generate_interlocking_segment function."""

    expected_coords = [(10, 0), (10, 20), (0, 20), (0, 60), (0, 100), (30, 100), (30, 60), (30, 20), (20, 20), (20, 0)]
    start_coord = (10, 0)
    stop_coord = (20, 0)
    neck_width = 10
    neck_height = 20
    head_width = 30
    head_height = 60

    interlocking_segment = generate_interlocking_segment(start_coord, stop_coord, neck_width, neck_height, head_width, head_height)
    assert interlocking_segment == expected_coords