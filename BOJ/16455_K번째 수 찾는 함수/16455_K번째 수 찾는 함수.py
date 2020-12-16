def kth(a,k):
    x = [0] * 10001
    y = [0] * 10001
    z = [0] * 100000
    for i in a:
        sh = i % 100000
        x[sh] += 1

    cnt = 0
    for i in range(10001):
        cnt += x[i]
        if cnt >= k:
            cnt -= x[i]
            q = i
            break
    
    for i in a:


    