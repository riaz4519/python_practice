
main_list = [str(i) for i in range(5)]
print(main_list)
diamond_list = []

for i in range(6):

    diamond_list.append((''.join(main_list[:i])).center(5))

print('\n'.join(diamond_list)+'\n'+'\n'.join(diamond_list[::-1][1:]))
