def count_substring(string, sub_string):
    len_of_sub = len(sub_string)
    new_string = string
    count = 0
    while sub_string in new_string:

        new_string = new_string[new_string.find(sub_string)+1:]
        count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)