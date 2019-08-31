
n = int(input())
l1 = []
pattern = []
for i in range(n-1,-1,-1):
    pattern.append(("".join(l1[0:n-i])+chr(97+i)+"-"+"".join(l1[::-1])).center(4*n-3,"-"))
    l1.append(chr(97+i)+"-")
else:
    pattern[n-1] = pattern[n-1][0:len(pattern[n-1])-1]

print("\n".join(pattern+pattern[0:len(pattern)-1][::-1]))


