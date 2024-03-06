#!/usr/bin/python3
""" A Python script to compute Pascal's triangle for any input number """


def pascal_triangle(n):
    """ A function that returns a list of lists of integers representing Pascal's triangle for a given number n. """
    triangle = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return triangle
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)
    # print(triangle)
    return triangle
