if __name__ == '__main__':
    N = int(input())

    main_list = []
    for _ in range(N):

        cmd = list(input().strip().split())

        if cmd[0] =='print':

            print(main_list)
        elif cmd[0] == 'insert':
            main_list.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == 'remove':
            main_list.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            main_list.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            main_list.sort()
        elif cmd[0] == 'pop':
            main_list.pop()
        elif cmd[0] == 'reverse':
            main_list.reverse()





