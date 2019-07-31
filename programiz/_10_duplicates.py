def duplicates(arr):

    dup = []
    for number in range(len(arr)):

        if arr[number] in arr[number+1:]:
            dup.append(arr[number])

    return  list(set(dup))

print(duplicates([0, 2, 0, 1, 3, 3]))