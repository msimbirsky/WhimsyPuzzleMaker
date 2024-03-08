"""Module for and generating altering line segments to assist processing and defining puzzle pieces."""

import numpy as np
import math

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    From: https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

def midpoint(p1, p2):
    """"Calculate the midpoint between two points."""
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def generate_anchor_point_coordinates(start_coord, stop_coord, neck_width, neck_height, head_width, head_height) -> list[tuple]:
    """"Given the start and stop coordinates, the 10 coordinates that can be used to generate the curved interlocking segment.

    Coordinates are needed to define the anchor points of a bezier curve for the interlocking segment.
    The points connect at the start and stop coordinates, and curves out to create a thinner (neck) and wider (head) segment.

    The start and stop coordinates are assumed to lie on the same line. The 
    anchor points should be rotated to be orthogonal to the line defined by the start and stop coordinates.
    
    Args:
        start_coord (tuple): The starting coordinate of the puzzle piece.
        stop_coord (tuple): The ending coordinate of the puzzle piece.
        neck_width (int): The width of the neck of the puzzle piece.
        neck_height (int): The height of the neck of the puzzle piece.
        head_width (int): The width of the head of the puzzle piece.
        head_height (int): The height of the head of the puzzle piece.

    Returns:
        list[tuple]: A list of anchor coordinates (x, y) that define a curve for the interlocking segment.
    """

    anchor_points = [None] * 10
    anchor_points[0] = start_coord
    anchor_points[9] = stop_coord

    # Calculate the coordinates of the neck and head of the puzzle piece
    anchor_points[1] = (start_coord[0], start_coord[1] + neck_height)
    anchor_points[2] = (start_coord[0] - (0.5*head_width - 0.5*neck_width), 
                        anchor_points[1][1])
    anchor_points[3] = (anchor_points[2][0], 
                        (anchor_points[2][1] + 0.5*head_height))
    anchor_points[4] = (anchor_points[3][0], 
                        (anchor_points[3][1] + 0.5*head_height))
    anchor_points[5] = (anchor_points[4][0] + head_width, anchor_points[4][1])
    anchor_points[6] = (anchor_points[5][0], (anchor_points[5][1] - 0.5*head_height))
    anchor_points[7] = (anchor_points[6][0], (anchor_points[6][1] - 0.5*head_height))
    anchor_points[8] = (anchor_points[7][0] - (0.5*head_width - 0.5*neck_width), 
                        anchor_points[7][1])

    # Rotate the coordinates to align with the base line
    origin = midpoint(start_coord, stop_coord)
    angle = math.atan2(stop_coord[1] - start_coord[1], stop_coord[0] - start_coord[0])
    anchor_points = [rotate(origin, point, angle) for point in anchor_points]

    return anchor_points


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

    anchor_points = generate_anchor_point_coordinates(start_coord, stop_coord, neck_width, neck_height, head_width, head_height)

    # Generate the bezier curve
    # todo: bezier curve(anchor_points)

    return []

# todo: graphical vector format