
#line part
def stright_line(x):
    print(('+ ' + '- ' * 4) * x + "+")
#space part
def space_line(x):
    print((((('|' + " " * 9) * x) + "|" + "\n") * 4)[:-1])

x = int(input())

for i in range(x):
    stright_line(x)
    space_line(x)
else:
    stright_line(x)