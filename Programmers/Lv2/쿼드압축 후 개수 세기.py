def solution(arr):
    answer = [0, 0]

    def quad(s1, e1, s2, e2):

        now = arr[s1][s2]
        for i in range(s1, e1):
            for j in range(s2, e2):
                if arr[i][j] != now:
                    m1 = (s1 + e1) // 2
                    m2 = (s2 + e2) // 2
                    direct1 = ((s1, m1), (m1, e1))
                    direct2 = ((s2, m2), (m2, e2))
                    for d1 in direct1:
                        for d2 in direct2:
                            quad(d1[0], d1[1], d2[0], d2[1])
                    return

        if now:
            answer[1] += 1
        else:
            answer[0] += 1

    quad(0, len(arr), 0, len(arr))

    return answer