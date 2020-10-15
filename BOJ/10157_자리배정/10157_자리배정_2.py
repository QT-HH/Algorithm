import sys
sys.stdin = open('input.txt')

C,R = map(int,input().split())
num = int(input())

if num>C*R:
    print(0)
else:
    start = 1
    x = 1
    y = 1
    val = 2*(C+R)-4
    while 1:
        if val < num:
            C-=2
            R-=2
            start = 1+val
            x += 1
            y += 1
            val += 2 * (C + R) - 4
        else:
            end1 = start+R-1
            end2 = start+R+C-2
            end3 = start+R+C+R-3
            if start <= num < end1:
                y+= num-start
            elif end1 <= num < end2:
                y+= R-1
                x+= num-end1
            elif end2 <= num < end3:
                y+= end3-num
                x+= C-1
            else:
                x+= val-num+1
            break

    print(x,y)