def kth(a,k):
    x = [0] * 10001
    y = [0] * 100000
    for i in a:
        sh, re = divmod(i,100000)
        x[sh] += 1
        y[sh].append(re)

    cnt = 0
    for i in x:
