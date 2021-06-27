def solution(phone_book):
    answer = True

    check_list = set()
    for i in phone_book:
        if len(i) == 2:
            check_list.add(i[0])
            continue
        for j in range(1, len(i)):
            check_list.add(i[:j])
    for i in phone_book:
        if i in check_list:
            answer = False
            break

    return answer