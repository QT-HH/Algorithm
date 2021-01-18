def solution(n):
    answer = []

    res = [[1, 3]]

    def hanoi(a, b, c):
        for j in res:
            tmp = [0, 0]
            for k in range(2):
                if j[k] == a:
                    tmp[k] = b
                elif j[k] == b:
                    tmp[k] = a
                else:
                    tmp[k] = c
            new.append(tmp)

    for i in range(1, n):
        new = []
        hanoi(2, 3, 1)
        new.append([1, 3])
        hanoi(1, 2, 3)
        res = new

    return res