import sys
sys.stdin = open('input.txt')

a = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

T = int(input())
for test_case in range(1, T + 1):
    x = input()
    if str(int(x[4:6])) in a.keys():
        if 0 < int(x[6:]) <= a[str(int(x[4:6]))]:
            print(f'#{test_case} {x[0:4]}/{x[4:6]}/{x[6:]}')
        else:
            print(f'#{test_case} {-1}')
    else:
        print(f'#{test_case} {-1}')