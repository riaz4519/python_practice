




# def expand(s, left, right):
#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         left -= 1
#         right += 1
#     return right-left-1
#
# s = 'GEEKSFORGEEKS'
# start, end = 0, 0
# for index in range(len(s)):
#     even_len = expand(s, index, index+1)
#     odd_len = expand(s, index, index)
#     length = max(even_len, odd_len)
#     if length > (end-start):
#         start = index - (length-1)/2
#         end = index +length/2
#
# print(s[start:end+1])

def longest_palindromic_substring(string):
  start = 0
  end = 0
  for i in range(len(string)):
    left, right = helper(string, i, i)
    if right - left > end - start:
      start = left
      end = right
    left, right = helper(string, i, i + 1)
    if right - left > end - start:
      start = left
      end = right
  return string[start:end + 1]

def helper(string, left, right):
  if right >= len(string):
    return (0, 0)
  start = left
  end = right
  while start >= 0 and end < len(string) and string[start] == string[end]:
    start -= 1
    end += 1
  return (start + 1, end - 1)

print(longest_palindromic_substring('abababa'))
print(longest_palindromic_substring('cbbd'))


