#!/usr/bin/python3
"""
Module for lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened.
    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or not all(isinstance(box, list) for box in boxes):
        return False

    keys = set([0])
    new_keys = set([0])
    while new_keys:
        box_index = new_keys.pop()
        for key in boxes[box_index]:
            if key not in keys and key < len(boxes):
                new_keys.add(key)
                keys.add(key)
    return len(keys) == len(boxes)

