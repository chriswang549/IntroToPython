# Christopher Wang
# christwang
# 110969745
# CSE 101
# Homework #2

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!


# Part I
def insurance(premium, age, gender):

    if age >= 18 and age < 21 and gender == 'Female':
     return (premium * .9)

    if age >= 18 and age < 21 and gender == 'Male':
        return (premium * 1.0)

    if age >= 21 and age <30:
        return (premium * .75)

    if age >= 30 and age < 60 and gender == 'Male':
        return (premium * .60)

    if age >= 30 and age <60 and gender == 'Female':
        return (premium *.70)

    if age >= 60:
        return (premium * 1.0)
    else:
        return -1




# Part II
def temperature_converter(value, scale_from, scale_to):
    if scale_from == 'K':
        if scale_to == 'C':
            return value - 273.15
        elif scale_to == 'F':
            return (value - 273.15) * 9/5 + 32
        else:
            return value

    if scale_from == 'C':
        if scale_to == 'F':
            return (value * 9/5) + 32
        elif scale_to == 'K':
            return value + 273.15
        else:
            return value

    if scale_from == 'F':
        if scale_to == 'C':
            return (value - 32) * 5/9
        elif scale_to == 'K':
            return (value - 32) * 5/9 + 273.15
        else:
            return value






# Part III
def row_boat(movements):
    integer = 0
    # for x, the elements, in the list of string movements
    for x in movements:
        if x == 'F':
            integer += 1
        elif x == 'B':
            if integer == 0:
                # does nothing if already at start position
                integer = integer
            else:
                # integer = integer - 1
                integer -= 1
        else:
            integer = 0
    return integer


# Part IV
def untangle(numbers, len_of_sublist):
    sub = []
    result = []

    for i in range(0, len(numbers)//len_of_sublist):
        for index in range(0, len(numbers)):
                if index%(len(numbers)//len_of_sublist) == i:
                    sub.append(numbers[index])
        result.append(sub)
        sub = []

    return result


# Part V
def car_rental(rentals):
    car_type = [0, 0, 0, 0]  # Income generated Sedan, Coupe, SUV, Hybrid (in that order)
    hours_free = 0
    income = 0

    for sub in rentals:
        if sub[0] == 'Student':
            hours_free = 3
        elif sub[0] == 'Faculty':
            hours_free = 2
        elif sub[0] == 'Visitor':
            hours_free = 1

        if sub[1] == 'Sedan':
            income = (sub[2] - hours_free)*10
            if income < 0:
                income = 0
            car_type[0] += income
        elif sub[1] == 'Coupe':
            income = (sub[2] - hours_free)*12
            if income < 0:
                income = 0
            car_type[1] += income
        elif sub[1] == 'SUV':
            income = (sub[2] - hours_free)*13
            if income < 0:
                income = 0
            car_type[2] += income
        elif sub[1] == 'Hybrid':
            income = (sub[2] - hours_free)*15
            if income < 0:
                income = 0
            car_type[3] += income
    return car_type


if __name__ == '__main__':
    # Testing Part I
    print("Part I: ")
    print("Testing insurance() with premium = 150, age = 20, gender = 'Female': " + str(insurance(150.0, 20, 'Female')))
    print("Testing insurance() with premium = 300, age = 25, gender = 'Male'  : " + str(insurance(300.0, 25, 'Male')))
    print("Testing insurance() with premium = 50,  age = 41, gender = 'Female': " + str(insurance(50.0, 41, 'Female')))
    print()

    # Testing Part II
    print("Part II: ")
    print("Testing temperature_converter() with value = 50, scale_from = 'K', scale_to = 'C': " + str(
        temperature_converter(50.0, 'K', 'C')))
    print("Testing temperature_converter() with value = 0,  scale_from = 'C', scale_to = 'F': " + str(
        temperature_converter(0.0, 'C', 'F')))
    print("Testing temperature_converter() with value = 32, scale_from = 'F', scale_to = 'C': " + str(
        temperature_converter(32.0, 'F', 'C')))
    print()

    # Testing Part III
    print("Part III: ")
    print("Testing row_boat() with movements = ['F', 'F', 'S', 'B', 'F']: " + str(
        row_boat(['F', 'F', 'S', 'B', 'F'])))
    print("Testing row_boat() with movements = ['S', 'S', 'S', 'B', 'S', 'B', 'B', 'B']: " + str(
        row_boat(['S', 'S', 'S', 'B', 'S', 'B', 'B', 'B'])))
    print("Testing row_boat() with movements = ['F', 'F', 'B', 'B', 'F', 'F', 'B', 'F', 'F']: " + str(
        row_boat(['F', 'F', 'B', 'B', 'F', 'F', 'B', 'F', 'F'])))
    print()

    # Testing Part IV
    print("Part IV: ")
    print("Testing untangle() with numbers = [1,2,3,4,5,6], len_of_sublist = 2: " + str(
        untangle([1, 2, 3, 4, 5, 6], 2)))
    print("Testing untangle() with numbers = [1,4,7,2,5,8,3,6,9], len_of_sublist = 3: " + str(
        untangle([1, 4, 7, 2, 5, 8, 3, 6, 9], 3)))
    print("Testing untangle() with numbers = [1,2,3], len_of_sublist = 1: " + str(untangle([1, 2, 3], 1)))
    print()

    # Testing Part V
    print("Part V: ")
    print("Testing car_rental() with rentals = [['Student','Coupe',4],['Faculty','Coupe',4],['Visitor','Coupe',4]]: " +
          str(car_rental([['Student', 'Coupe', 4], ['Faculty', 'Coupe', 4], ['Visitor', 'Coupe', 4]])))
    print("Testing car_rental() with rentals = [['Student','Coupe',4],['Faculty','SUV',4],['Visitor','Hybrid',4],['Visitor','Sedan',4]]: " +
          str(car_rental([['Student', 'Coupe', 4], ['Faculty', 'SUV', 4], ['Visitor', 'Hybrid', 4], ['Visitor', 'Sedan', 4]])))
    print("Testing car_rental() with rentals = [['Student','Coupe',3],['Faculty','SUV',2],['Visitor','Hybrid',1],['Visitor','Sedan',4]]: " +
          str(car_rental([['Student', 'Coupe', 3], ['Faculty', 'SUV', 2], ['Visitor', 'Hybrid', 1], ['Visitor', 'Sedan', 4]])))
    print()
