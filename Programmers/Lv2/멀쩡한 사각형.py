def solution(w, h):
    answer = w * h

    if w == h:
        answer -= w
    else:
        if w <= h:
            a, b = h, w
        else:
            a, b = w, h

        while b != 0:
            r = a % b
            a, b = b, r

        x = w // a
        y = h // a

        if x <= y:
            x, y = y, x

        answer -= (y + y + (x - y - 1)) * a

    return answer