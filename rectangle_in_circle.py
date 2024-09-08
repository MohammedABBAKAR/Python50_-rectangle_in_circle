
# todo Rectangle in Circle
# ? Create a function that takes three numbers — the width and height of a rectangle, 
# ? and the radius of a circle — and returns True if the rectangle can fit inside the circle, False if it can't.

# * Examples
# * rectangle_in_circle(8, 6, 5) ➞ True

# * rectangle_in_circle(5, 9, 5) ➞ False

# * rectangle_in_circle(4, 7, 4) ➞ False
# ! Notes
# N/A



# todo Steps:
# ? 1-The diagonal d of the rectangle can be calculated using the Pythagorean theorem:
#  *  w**2 + h**2 = c**2

# ? where w is the width and h is the height of the rectangle.

# ? 2-The diameter of the circle is 2*r, where r is the radius of the circle.

# ?  3-If the diagonal of the rectangle is less than or equal to the diameter of the circle, the rectangle can fit inside the circle.




import math

def rectangle_in_circle(width, height, radius):
    diagonal = math.sqrt(width**2 + height**2)
    diameter = 2 * radius
    return diagonal <= diameter


print(rectangle_in_circle(8, 6, 5))  
print(rectangle_in_circle(5, 9, 5)) 
print(rectangle_in_circle(4, 7, 4)) 
