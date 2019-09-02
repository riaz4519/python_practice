
def times_table():

    x = input('please enter a number')

    try:
        x = int(x)

        for i in range(x+1):
            for j in range(x+1):
                print('%3s' % (i*j),end="")
            print()

    except ValueError:
        print('oops error ')
        x = input('want to try again:(y/n)')

        if x == 'y':
            times_table()
        else:
            return
times_table()