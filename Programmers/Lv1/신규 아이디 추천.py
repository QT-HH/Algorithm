def solution(new_id):
    answer = ''
    special = {'-', '_', '.'}
    new_id = list(new_id.lower())

    before = ''
    for i in range(len(new_id)):
        if not new_id[i].isalpha() and not new_id[i].isdigit() and new_id[i] not in special:
            new_id[i] = ''
        elif new_id[i] == '.' and before == '.':
            new_id[i] = ''
        else:
            before = new_id[i]

    new_id = list(''.join(new_id))

    if new_id and new_id[0] == '.':
        new_id.pop(0)
    if new_id and new_id[-1] == '.':
        new_id.pop()

    if not new_id:
        new_id = ['a']

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id.pop()
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id.append(new_id[-1])

    answer = ''.join(new_id)

    return answer