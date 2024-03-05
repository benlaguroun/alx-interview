#!/usr/bin/python3
"""
0-main
"""
from pascal_triangle import pascal_triangle, print_triangle

def main():
    """
    Main function
    """
    triangle = pascal_triangle(5)
    print_triangle(triangle)

if __name__ == "__main__":
    main()

