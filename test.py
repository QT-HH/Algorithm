def Sum3(x, y, z):
    tmp = 0
    for i in range(x, y+1, z):
        tmp += 1
    return tmp

return_value = Sum3(1, 100, 2)
print(' 10 ~ 100까지 홀수 합 ==> ', return_value)

return_value = Sum3(2, 100, 2)
print(' 1 ~ 100까지 짝수 합 ==> ', return_value)

return_value = Sum3(10, 1000, 10)
print(' 10 ~ 1000까지 10의 배수 합 ==> ', return_value)