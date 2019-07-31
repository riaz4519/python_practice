def swap_case(s):

    new_string = ""

    for lat in s:

        if lat.isupper() == True:
            new_string += (lat.lower())
        else:
            new_string += (lat.upper())

    return new_string

if __name__ == '__main__':
    s = input().strip()
    result = swap_case(s)
    print(result)