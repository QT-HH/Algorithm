def find(cnt,tmp):
    if cnt > 10:
        return
    elif cnt == 10:
        if set(tmp) not in result:
            result.append(set(tmp))
        return
    else:
        for i in range(10):
            if nums[i] not in tmp:
                tmp.append(nums[i])
                find(cnt+nums[i],tmp)
                tmp.pop()

nums = list(range(1,11))
result = []
tmp = []

find(0,tmp)

print(result)