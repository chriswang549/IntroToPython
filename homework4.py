# Christopher Wang
# christwang
# 110969745
# CSE 101
# Homework #4

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!


def pretty_print(keys_per_line, object, return_type=None):
    string = ''

    assert keys_per_line > 0, 'Invalid keys_per_line. Please provide a value > 0.'

    if type(object) == dict:
        value = list(object.values())
        key = list(object.keys())
        for i in range(len(object)):
            if i < len(object) - 1:
                if (i % keys_per_line != 0) or i == 0:
                    string += str(key[i]) + ' -> ' + str(value[i]) + ' \t'
                else:
                    string += '\n' + str(key[i]) + ' -> ' + str(value[i]) + ' \t'
            else:
                if i % keys_per_line != 0:
                    string += str(key[i]) + ' -> ' + str(value[i]) + '\n'
                else:
                    string += '\n' + str(key[i]) + ' -> ' + str(value[i]) + '\n'
    if return_type is None:
        print(string)
    else:
        return string


# Part I
def updown_encrypt(plaintext, num_rows):
    encryptedWord = ''

    if len(plaintext) == 0:
        for i in range(num_rows):
            encryptedWord += '%'
        return encryptedWord
    if num_rows <= 0:
        return plaintext

    remainder = 0
    if len(plaintext) % num_rows != 0:
        remainder = num_rows - len(plaintext) % num_rows

    length = (int)(len(plaintext) / num_rows) + remainder
    num_arrays = []

    for i in range(length):
        num_arrays.append([])

    for i in range(len(num_arrays)):  # loop through all array
        if len(plaintext) >= num_rows:
            for numChar in range(num_rows):
                word = plaintext[numChar]
                num_arrays[i].append(word)
        else:
            for rest in range(len(plaintext)):
                word = plaintext[rest]
                num_arrays[i].append(word)
        plaintext = plaintext[num_rows:]

    for i in range(len(num_arrays)):
        if len(num_arrays[i]) != num_rows:
            for j in range(len(num_arrays[i]), num_rows):
                num_arrays[i].append('%')
    for i in range(1, length):
        if i % 2 != 0:
            num_arrays[i].reverse()

    for i in range(len(num_arrays)):
        count = 0
        for j in range(len(num_arrays[i])):
            if num_arrays[i][j] == '%':
                count += 1
                if count == num_rows:
                    for times in range(num_rows):
                        num_arrays[i].pop()

    newList = []
    for i in range(len(num_arrays)):
        if len(num_arrays[i]) != 0:
            newList.append(num_arrays[i])

    for i in range(num_rows):
        letters = [item[i] for item in newList]
        encryptedWord += ''.join(letters)
    return encryptedWord

# Part II
def updown_decrypt(encrypted, num_rows):
    counter = -1
    direction = 1
    output = ''
    char_grid = []
    for i in range(num_rows):
        char_grid.append([])
    if len(encrypted) <= 0:
        return None
    if num_rows < 1:
        return encrypted

    for i in range(len(encrypted)):
        char_grid[i // (len(encrypted) // num_rows)].append(encrypted[i])

    for i in range(len(encrypted)):
        counter += direction
        if counter == num_rows or counter == -1:
            direction *= -1
            counter += direction
        if (char_grid[counter][i // num_rows] != '%'):
            output += char_grid[counter][i // num_rows]

    return output


# Part III
def map_char_to_coords(filename):
    d = {}
    f = open(filename)

    for num, line in enumerate(f):
        line = line.strip() # separate each letter in line
        letters = line.split() # put them in array to hold indexes
        for c in letters: # for each letter in the current line
            if c not in d:# if letter doesnt exist in dictionary
                d[c] = (num + 1, letters.index(c) + 1)
                # add key letter and it's index as the value
    return d



# Part IV
def map_coords_to_char(filename):
    num_line = 1
    d = {}
    f = open(filename)

    for line in f:
        line = line.strip()
        letters = line.split()
        for i, c in enumerate(letters):
            d[(num_line, i + 1)] = c
        num_line += 1
    return d




# Part V
def dc_encrypt(plaintext, filename):
    #generate coordinate position of each character in filename
    char_to_coords = map_char_to_coords(filename)

    row = ''
    column = ''
    list1 = [] # list of all integers to pair later
    list2 = [] # list that holds the paired integers from list1

    # getting rows columns of the character
    for char in plaintext:
        r, c = char_to_coords[char]
        row += str(r) + ' '
        column += str(c) + ' '

    splitRow = row.split() # puts them in list to access indexes
    splitColumn = column.split() # puts them in list to access indexes

    for i in splitRow:
        list1.append(int(i))

    for j in splitColumn:
        list1.append(int(j))

    # combining the two coordinates
    for i in range(0, len(list1), 2):
        list2.append(int(str(list1[i]) + str(list1[i + 1])))

    coords_to_char = map_coords_to_char(filename)

    encrypt = ''

    # encryption
    for i in list2:
        s = str(i) # paired integer
        coord1 = int(s[0]) # first digit
        coord2 = int(s[1]) # second digit
        encrypt += coords_to_char[(coord1, coord2)] # char based on coord

    return encrypt


# Part VI
def dc_decrypt(encrypted, filename):
    # generate coordinate position of each character in filename
    char_to_coords = map_char_to_coords(filename)

    numbers = ''
    # getting rows columns of the character
    for char in encrypted:
        r, c = char_to_coords[char]
        numbers += str(r) + ' '
        numbers += str(c) + ' '

    half1 = []
    half2 = []
    numList = numbers.split()
    length = (int)(len(numList)/2)

    for i in numList[:length]:
        half1.append(i)
    for j in numList[length:]:
        half2.append(j)

    list = []
    # combining the two coordinates
    for i in range(len(half1)):
        list.append(int(str(half1[i])))
        list.append(int(str(half2[i])))
    print(list)
    coords_to_char = map_coords_to_char(filename)

    decrypt = ''

    # encryption
    for i in range(0, len(list), 2):
        coord1 = list[i]  # first digit (row)
        coord2 = list[i+1]  # second digit (column)
        decrypt += coords_to_char[(coord1, coord2)]  # char based on coord

    return decrypt


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.
# Upload your homework3.py file to CodeLoad to see how it matches up against other
# test cases!
if __name__ == '__main__':
    # Testing Part I
    print("##### Part I ##### ")
    print("Testing snake_encrypt() with plaintext = 'AMERICA', num_cols = 7: "
          + str(updown_encrypt('AMERICA', 7)))
    print("Testing snake_encrypt() with plaintext = 'STONYBROOKUNIV', num_cols = 4: "
          + str(updown_encrypt('STONYBROOKUNIV', 4)))
    print("Testing snake_encrypt() with plaintext = 'CHICKENWINGS', num_cols = -2: "
          + str(updown_encrypt('CHICKENWINGS', -2)))
    print("Testing snake_encrypt() with plaintext = '', num_cols = 5: "
          + str(updown_encrypt('', 5)))
    print()

    # Testing Part II
    print("##### Part II ##### ")
    print("Testing snake_decrypt() with encrypted = 'AMERICA', num_cols = 7: "  # Simple case
          + str(updown_decrypt('AMERICA', 7)))
    print("Testing snake_decrypt() with encrypted = 'SOO%TRK%OBUVNYNI', num_cols = 4: "  # Multi Lines case
          + str(updown_decrypt('SOO%TRK%OBUVNYNI', 4)))
    print("Testing snake_decrypt() with encrypted = 'CHICKENWINGS', num_cols = -2: "  # Invalid step case
          + str(updown_decrypt('CHICKENWINGS', -2)))
    print()

    # Testing Part III
    print("##### Part III ##### ")
    print("Testing map_char_to_coords with filename = 'key1.txt': ")
    pretty_print(4, map_char_to_coords('key1.txt'), None)
    print("Testing map_char_to_coords with filename = 'key2.txt': ")
    pretty_print(4, map_char_to_coords('key2.txt'), None)
    print("Testing map_char_to_coords with filename = 'key3.txt': ")
    pretty_print(4, map_char_to_coords('key3.txt'), None)

    # Testing Part IV
    print("##### Part IV ##### ")
    print("Testing map_coords_to_char with filename = 'key1.txt': ")
    pretty_print(4, map_coords_to_char('key1.txt'), None)
    print("Testing map_coords_to_char with filename = 'key2.txt': ")
    pretty_print(4, map_coords_to_char('key2.txt'), None)
    print("Testing map_coords_to_char with filename = 'key3.txt': ")
    pretty_print(4, map_coords_to_char('key3.txt'), None)

    # Testing Part V
    print("##### Part V ##### ")
    print("Testing dc_encrypt with plaintext = 'STONYBROOK', filename = 'key1.txt': "
          + str(dc_encrypt('STONYBROOK', 'key1.txt')))
    print("Testing dc_encrypt with plaintext = 'SUFFOLKCOUNTY', filename = 'key1.txt': "
          + str(dc_encrypt('SUFFOLKCOUNTY', 'key1.txt')))
    print("Testing dc_encrypt with plaintext = 'CSE101ISEASY', filename = 'key2.txt': "
          + str(dc_encrypt('CSE101ISEASY', 'key2.txt')))
    print("Testing dc_encrypt with plaintext = 'PASSWORD89ASHD891NE21D', filename = 'key3.txt': "
          + str(dc_encrypt('PASSWORD89ASHD891NE21D', 'key3.txt')))

    # Testing Part VI
    print("\n##### Part VI #####")
    print("Testing dc_decrypt with encrypted = 'J418FR9939', filename = 'key1.txt': "
          + str(dc_decrypt('J418FR9939', 'key1.txt')))
    print("Testing dc_decrypt with encrypted = 'GFOOKXEFOBTK3', filename = 'key1.txt': "
          + str(dc_decrypt('GFOOKXEFOBTK3', 'key1.txt')))
    print("Testing dc_decrypt with encrypted = 'J6GI6SJR0SEY', filename = 'key2.txt': "
          + str(dc_decrypt('J6GI6SJR0SEY', 'key2.txt')))
    print("Testing dc_decrypt with encrypted = 'PBW98AY8E77AROT9SN93J3', filename = 'key3.txt': "
          + str(dc_decrypt('PBW98AY8E77AROT9SN93J3', 'key3.txt')))
