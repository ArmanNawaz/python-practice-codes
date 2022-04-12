if __name__ == '__main__':
    arr = [1,2,3,6,7,8,9,10,15,20,25]

    diff = []

    for i in range(1, len(arr)):
        diff.append(arr[i] - arr[i-1])
    count = 1
    i = 0
    ans = 0
    while i < len(diff):
        count = 1
        while i < len(diff)-1 and diff[i] == diff[i+1]:
            count += 1
            i += 1
        i += 1
        ans += count * (count - 1) // 2
print(ans)

