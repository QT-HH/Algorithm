def solution(s):
    answer = 1
    length = len(s)
    i = 0

    while i < length:

        if i < length - 1 and s[i] == s[i + 1]:
            x = 1
            while 1:
                l = i - x
                r = i + 1 + x
                if 0 <= l and r < length and s[l] == s[r]:
                    x += 1
                else:
                    answer = max(answer, x * 2)
                    break

        x = 1
        while 1:
            l = i - x
            r = i + x
            if 0 <= l and r < length and s[l] == s[r]:
                x += 1
            else:
                answer = max(answer, x * 2 - 1)
                break
        i += 1

    return answer