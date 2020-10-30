import sys
sys.stdin = open('input.txt')

def dfs(x,tmp):
    if x >= N:
        result_max[0] = max(result_max[0],tmp)
        result_min[0] = min(result_min[0],tmp)
    else:
        for i in range(4):
            if opts[i]:
                if i == 0:
                    n_tmp = tmp + nums[x]
                elif i == 1:
                    n_tmp = tmp - nums[x]
                elif i == 2:
                    n_tmp = tmp * nums[x]
                else:
                    n_tmp = int(tmp/nums[x])
                opts[i] -= 1
                dfs(x+1,n_tmp)
                opts[i] += 1


T = int(input())
for t in range(1,T+1):
    N = int(input())
    opts = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    result_max = [float('-inf')]
    result_min = [float('inf')]

    dfs(1,nums[0])

    print('#{} {}'.format(t,result_max[0]-result_min[0]))
