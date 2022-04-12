if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())

        rem = n % 4

        ignore = [1, 2, 3, 5, 7, 11]
        if n in ignore:
            print(-1)
        elif rem == 0 or rem == 2:
            print(n//4)
        else:
            print(n//4 - 1)