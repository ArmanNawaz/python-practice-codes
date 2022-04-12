def solve(tickets):

    freq = [0] * 1024
    for ticket in tickets:
        mask = 0
        for i in ticket:
            mask = mask | (1 << int(i))
        freq[mask] += 1

    ans = 0

    for i in range(1023):
        if freq[i] == 0: continue
        for j in range(i+1, 1024):
            if i | j == 1023:
                ans += freq[i] * freq[j]
    ans += (freq[1023] * (freq[1023] - 1)) // 2
    return ans


if __name__ == '__main__':
    # n = int(input())

    # tickets = []
    # for _ in range(n):
    #     tickets.append(input())
    tickets = [
'129300455',
'5559948277',
'012334556',
'56789',
'123456879']
    print(solve(tickets))

    