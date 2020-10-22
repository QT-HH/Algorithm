import sys
sys.stdin = open('input.txt')


def find(a,b,c,d):
    if b == a:
        return 1

    for i in board[d]:
        



board = {
    'c':['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
    'd':[0,1,2,3,4,5,6,7,8,9]
}

ip = input()
cnt = 0
l = len(ip)
