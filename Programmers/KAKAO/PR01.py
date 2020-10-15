def solution(new_id):
    new_id = list(new_id)
    exc = {'.', '-', '_'}
    i = 0
    while i < len(new_id):
        if new_id[i].isalpha():
            new_id[i] = new_id[i].lower()

        if new_id[i] in exc or new_id[i].isalpha() or new_id[i].isdigit():
            i+=1
            continue
        else:
            new_id.pop(i)
            continue

        i += 1

    i = 0
    while i < len(new_id):
        if new_id[i] == '.':
            j = i + 1
            cnt = j
            while 1:
                if j > len(new_id) - 1:
                    new_id[i:j] = ['.']
                    break
                if new_id[j] == '.':
                    j += 1
                    continue
                else:
                    new_id[i:j] = ['.']
                    break
        i += 1

    if len(new_id) > 0 and new_id[0] == '.':
        new_id.pop(0)
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id.pop()

    if new_id == []:
        new_id.append('a')

    if len(new_id) > 15:
        new_id = new_id[:15]
    elif len(new_id) < 3:
        while len(new_id) < 3:
            new_id.append(new_id[-1])

    answer = ''.join(new_id)
    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
solution(new_id)