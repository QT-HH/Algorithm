def mat(a,b,c,d,n):
    if n >=60:
        return
    n+=1
    q = (a*a+b*c)%1000000
    w = (a*b+b*d)%1000000
    e = (c*a+d*c)%1000000
    r = (c*b+d*d)%1000000
    dp.append((q,w,e,r))
    return mat(q,w,e,r,n)

def cal(x,y,i):
    i+=1
    q = (x[0]*y[0]+x[1]*y[2])%1000000
    w = (x[0]*y[1]+x[1]*y[3])%1000000
    e = (x[2]*y[0]+x[3]*y[2])%1000000
    r = (x[2]*y[1]+x[3]*y[3])%1000000
    if i>= len(mu):
        return w
    return cal((q,w,e,r),dp[mu[i]],i)

n = int(input())
mu = []
dp=[(1,1,1,0)]
result = 0
if n==0:
    print(0)
else:
    for i in range(59,-1,-1):
        if n >= 1<<i:
            n -= 1<<i
            mu.append(i)
    mat(1,1,1,0,0)
    if len(mu)==1:
        print(dp[mu[0]][1])
    else:
        result = cal(dp[mu[0]],dp[mu[1]],1)
        print(result%1000000)
