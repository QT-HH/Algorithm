def solution(genres, plays):
    answer = []
    songs = dict()
    cnts = dict()
    for i in range(len(genres)):
        if songs.get(genres[i]):
            if songs[genres[i]].get(plays[i]):
                songs[genres[i]][plays[i]].append(i)
            else:
                songs[genres[i]][plays[i]] = [i]
            cnts[genres[i]] += plays[i]
        else:
            songs[genres[i]] = {plays[i]: [i]}
            cnts[genres[i]] = plays[i]

    print(songs)
    for i in sorted(cnts.items(), reverse=True, key=lambda x: x[1]):
        tmp1 = sorted(songs[i[0]], reverse=True)[:2]
        tmp_list = []
        for j in tmp1:
            tmp_list.extend(sorted(songs[i[0]][j])[:2])

        answer.extend(tmp_list[:2])

    return answer