if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]

    print(sorted(list(set(arr)),reverse = True)[1])