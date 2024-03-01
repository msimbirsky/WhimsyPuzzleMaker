"""Module for and generating altering line segments to assist processing and defining puzzle pieces."""

import numpy as np


def generate_interlocking_segment(start_coord, stop_coord, neck_width, neck_height, head_width, head_height) -> list[tuple]:
    """Given the start and stop coordinates, generate a curve that represents an interlocking puzzle piece.
    
    Args:
        start_coord (tuple): The starting coordinate of the puzzle piece.
        stop_coord (tuple): The ending coordinate of the puzzle piece.
        neck_width (int): The width of the neck of the puzzle piece.
        neck_height (int): The height of the neck of the puzzle piece.
        head_width (int): The width of the head of the puzzle piece.
        head_height (int): The height of the head of the puzzle piece.
        
    Returns:
        list[tuple]: A list of coordinates (x, y) that define a curve for the interlocking segment.
    """

    # Calculate the slope of the line between the start and stop coordinates
    slope = (stop_coord[1] - start_coord[1]) / (stop_coord[0] - start_coord[0])

    # Calculate the angle of the line between the start and stop coordinates
    angle = np.arctan(slope)

    anchor_points = [None] * 10
    anchor_points[0] = start_coord
    anchor_points[9] = stop_coord
    # Calculate the coordinates of the neck and head of the puzzle piece
    anchor_points[1] = (start_coord[0] - np.cos(angle), start_coord[1] + neck_height)
    neck_coord = (start_coord[0] + neck_width * np.cos(angle), start_coord[1] + neck_height * np.sin(angle))
    head_coord = (stop_coord[0] - head_width * np.cos(angle), stop_coord[1] - head_height * np.sin(angle))

    # Generate the interlocking segment
    interlocking_segment = [start_coord, neck_coord, head_coord, stop_coord]

    return interlocking_segment