if __name__ == "__main__":
    n = int(input())
    marksheet = [[input(),float(input())] for _ in range(n)]
    secondLarge = sorted(list(set([mark for name,mark in marksheet])))[1]

    print('\n'.join(sorted([name for name,mark in marksheet if mark == secondLarge])))


