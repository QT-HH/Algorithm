import sys
sys.stdin = open('input.txt')



for test in range(1,11):
    t = int(input())
    ladder = [list(map(int,input().split())) for i in range(100)]
    arrive = ladder[99].index(2)
    i = 99
    j = 0

    while i>0:
        if arrive+j > 0 and ladder[i][arrive+j-1]:
            while arrive+j > 0 and ladder[i][arrive+j-1]:
                j-=1
            i-=1
            continue

        if arrive+j < 99 and ladder[i][arrive+j+1]:
            while arrive+j < 99 and ladder[i][arrive+j+1]:
                j+=1
            i-=1
            continue

        i-=1


    print(f'#{test} {arrive+j}')