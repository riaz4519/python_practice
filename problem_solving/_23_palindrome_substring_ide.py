
def palindrome_string(s):

    new_s = ['@']
    for single_string in s:
        new_s.append('#')
        new_s.append(single_string)
    else:
        new_s.append('#')
        new_s.append('$')
    #place holder for position wise palindrome length

    new_s_p = [0 for _ in range(len(new_s))]
    center_s, right_b = 0, 0
    for i in range(1, (len(new_s)-1)):
        mirror = center_s - (i - center_s)

        if i < right_b:
            new_s_p[i] = min(right_b-i, new_s_p[mirror])

        while new_s[i+(1+new_s_p[i])] == new_s[i-(1+new_s_p[i])]:
            new_s_p[i] += 1

            if i+new_s_p[i] > right_b:

                center_s = i
                right_b = i + new_s_p[i]

    max_of_new_s_p = max(new_s_p)
    index_of_max = new_s_p.index(max_of_new_s_p)
    final_s_list = new_s[(index_of_max+1-max_of_new_s_p):index_of_max+max_of_new_s_p]

    return  ''.join([i for i in final_s_list if i != '#' ])


print(palindrome_string('babcbabcbaccba'))

# work just with the odd

