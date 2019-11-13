# Christopher Wang
# christwang
# 110969745
# CSE 101
# Homework #1

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!

import math

# Part I
def compute(x, y):
    return (x*y) / (y+2) - y/x


# Part II
def find_area(r):
    return (3.14 * r**2) - (2*r**2)


# Part III
def gas_refill(dis, mins, price, total_mins):
    return (dis / mins) * (total_mins / 20) * price


# Part IV
def heat_transfer(m, c, initial, final):
    return m * c * (final - initial) / (m * 4.18)


# Part V
def rocket_area(c, r, h, b):
    return (2 * math.pi * r * h) + (math.pi * r ** 2) + ((4 * b ** 2) / 2) + ((math.pi * r) *(math.sqrt(c**2 + r**2)))


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.
# Upload your lab2.py file to CodeLoad to see how it matches up against other
# test cases!
if __name__ == '__main__':
    # Testing Part I
    print("Part I: ")
    print("Testing compute() with x = 5, y = 2: " + str(compute(5, 2)))
    print("Testing compute() with x = 3, y = 4: " + str(compute(3, 4)))
    print("Testing compute() with x = 8, y = 8: " + str(compute(8, 8)))
    print()

    # Testing Part II
    print("Part II: ")
    print("Testing find_area() with r = 1: " + str(find_area(1)))
    print("Testing find_area() with r = 4: " + str(find_area(4)))
    print("Testing find_area() with r = 10: " + str(find_area(10)))
    print()

    # Testing Part III
    print("Part III: ")
    print("Testing gas_refill() with dis = 10, mins = 10, price = 2.0, total_mins = 30: " +
          str(gas_refill(10, 10, 2.0, 30)))  # Simple Case #1
    print("Testing gas_refill() with dis = 30, mins = 15, price = 2.62, total_mins = 17: " +
          str(gas_refill(30, 15, 2.62, 17)))  # Simple Case #2
    print("Testing gas_refill() with dis = 16, mins = 5, price = 1.77, total_mins = 9: " +
          str(gas_refill(16, 5, 1.77, 9)))  # Simple Case #3
    print()

    # Testing Part IV
    print("Part IV: ")
    print("Testing heat_transferred() with m = 550, c = 2.32, initial = 16, final = 46: " +
          str(heat_transfer(550, 2.32, 16, 46)))  # Simple Case #1
    print("Testing heat_transferred() with m = 426, c = 5.53, initial = 39, final = 100: " +
          str(heat_transfer(426, 5.53, 39, 100)))  # Simple Case #1
    print("Testing heat_transferred() with m = 50, c = 3.31, initial = 88.6, final = 87.1: " +
          str(heat_transfer(50, 3.31, 88.6, 87.1)))  # Heat Lost Case
    print()

    # Testing Part V
    print("Part V: ")
    print("Testing rocket_area() with c = 2, r = 2, h = 5, b = 1: " +
          str(rocket_area(2, 2, 5, 1)))  # Simple Case #1
    print("Testing rocket_area() with c = 12, r = 5, h = 3, b = 1: " +
          str(rocket_area(12, 5, 3, 1)))  # Simple Case #2
    print("Testing rocket_area() with c = 7, r = 4, h = 20, b = 3: " +
          str(rocket_area(7, 4, 20, 3)))  # Simple Case #3
    print()