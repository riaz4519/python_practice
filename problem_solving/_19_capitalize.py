def solve(s):
    string_split = s.split()

    data_ret = [word.capitalize() for word in string_split]
    space = " "
    return space.join(data_ret)

print(solve(input()))