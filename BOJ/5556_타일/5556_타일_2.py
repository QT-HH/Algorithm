#!/usr/bin/env python3

import sys
sys.stdin = open('input.txt')

def main():
    n = int(sys.stdin.readline())
    for _ in range(int(sys.stdin.readline())):
        a, b = map(int, sys.stdin.readline().split())
        print((1, 2, 3)[min(a - 1, b - 1, n - a, n - b) % 3])

if __name__ == '__main__':
    sys.exit(main())