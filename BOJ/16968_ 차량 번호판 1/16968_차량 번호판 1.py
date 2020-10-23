import sys
sys.stdin = open('input.txt')


def find(a,b,c,d):
    # a = 문자열 길이(마지막 인덱스 위치)
    # b = 현재 인덱스 위치
    # c = 이전 인덱스에 들어간 데이터
    # d = 현재 인덱스의 문자
    for i in board[d]:
        if i == c:
            continue
        elif b == a:
            cnt[0] += 1
        else:
           find(a,b+1,i,ip[b+1])



board = {
    'c':['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
    'd':[0,1,2,3,4,5,6,7,8,9]
}

ip = input()
cnt = [0]
l = len(ip)-1
find(l,0,-1,ip[0])
print(cnt[0])