
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


print(palindrome_string('439671913169768210880962528779044921214653729760961967312219315729051436700988975291224467598181008351941131051570812459210249369106411836951001002340483417565507341626341463773029280521487959984058684941220744882834172187098695773189403499087280909110119181670989031493301341331552586696953063188448'))
# import sys
#
#
# def main(lines):
#     # このコードは標準入力と標準出力を用いたサンプルコードです。
#     # このコードは好きなように編集・削除してもらって構いません。
#     # ---
#     # This is a sample code to use stdin and stdout.
#     # Edit and remove this code as you like.
#
#     new_lines = ['@']
#     for single_index_value in lines:
#
#         new_lines.append('#')
#         new_lines.append(single_index_value)
#
#     else:
#         new_lines.append('#')
#         new_lines.append('$')
#
#     new_lines_place_holder = [0 for _ in range(len(new_lines))]
#
#     middle_string = 0
#     boundary_right = 0
#
#     for iterate_index in range(1, (len(new_lines) - 1)):
#
#         string_mirror = middle_string - (iterate_index - middle_string)
#
#         if iterate_index < boundary_right:
#             new_lines_place_holder[iterate_index] = min(boundary_right - iterate_index,
#                                                         new_lines_place_holder[string_mirror])
#
#         while new_lines[iterate_index + (1 + new_lines_place_holder[iterate_index])] == new_lines[
#             iterate_index - (1 + new_lines_place_holder[iterate_index])]:
#
#             new_lines_place_holder[iterate_index] += 1
#
#             if iterate_index + new_lines_place_holder[iterate_index] > boundary_right:
#                 middle_string = iterate_index
#                 boundary_right = iterate_index + new_lines_place_holder[iterate_index]
#
#     maximum_value_place_holder = max(new_lines_place_holder)
#
#     position_of_max_value = new_lines_place_holder.index(maximum_value_place_holder)
#
#     palindrome_final_list = new_lines[(
#                                                   position_of_max_value + 1 - maximum_value_place_holder): position_of_max_value + maximum_value_place_holder]
#
#     print(''.join([output_single for output_single in palindrome_final_list if output_single != '#']))
#
#     # for i, v in enumerate(lines):
#     #     print("line[{0}]: {1}".format(i, v))
#
#
# if __name__ == '__main__':
#     lines = []
#     for l in sys.stdin:
#         lines.append(l.rstrip('\r\n'))
#     main(lines)

