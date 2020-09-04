def check(word, longword):
    while (1):
        if len(longword) < len(word):
            return 0
        c = longword[len(word)-1]
        for i in range(len(word))[::-1]:
            if c == word[i]:
                print(i,longword[len(word)-1-i:2*len(word)-1-i])
                if longword[len(word)-1-i:2*len(word)-1-i] == word:
                    return 1
        else:
            longword = longword[len(word):]


import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    word = input()
    longword = input()
    print(f'#{test_case} {check(word, longword)}')
