import collections
def solution(a):
    left = collections.deque()
    right = collections.deque()
    left.append(a[0])
    right.extend(a[1:])
    left_min = min(left)
    right_min = min(right)
    res = {a[0],a[-1]}
    while right:
        center = right.popleft()
        if center == right_min:
            right_min = min(right)
        res.append(min(left_min,center,right_min))

        left.append(center)
        if center < left_min:
            left_min = center

    answer = len(res)
    return answer