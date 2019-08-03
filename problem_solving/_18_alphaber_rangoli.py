n = int(input())

pattern = [ chr(97+i).center(n*3,'-') for i in range(n-1,0,-1)]

print("\n".join(pattern))
