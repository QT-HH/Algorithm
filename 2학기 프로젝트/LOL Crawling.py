import json
import sys
sys.stdin = open('inputLOL.txt', 'rt', encoding='UTF8')

team = {
    "담원 기아":33,
    "DRX":34,
    "젠지e스포츠":35,
    "아프리카 프릭스":36,
    "T1":37,
    "kt 롤스터":38,
    "리브 샌드박스":39,
    "농심 레드포스":40,
    "한화생명e스포츠":41,
    "프레딧 브리온":42,
}
team_name = {
    "담원 기아":"담원기아",
    "DRX":"DRX",
    "젠지e스포츠":"젠지",
    "아프리카 프릭스":"아프리카",
    "T1":"T1",
    "kt 롤스터":"KT",
    "리브 샌드박스":"리브샌박",
    "농심 레드포스":"농심",
    "한화생명e스포츠":"한화",
    "프레딧 브리온":"프레딧 브리온",
}

res = []
i = 1
while True:
    try:
        events1 = {}
        events2 = {}
        events1["id"] = i
        events2["id"] = i+1
        events1["event_no"] = 3
        events2["event_no"] = 3

        x,y = input().split('월')
        y,z = y.split('(')
        x = x[-1]
        y = y[:-1]
        events1["start"] = "2021-{}-{}".format(x,y)
        events2["start"] = "2021-{}-{}".format(x,y)

        events1["start_time"] = "17:00"
        events2["start_time"] = "20:00"
        input()
        team1,team2 = input().split("-")
        team3,team4 = input().split("-")

        events1["team1_id"] = team[team1[1:]]
        events1["team2_id"] = team[team2]
        events2["team1_id"] = team[team3[1:]]
        events2["team2_id"] = team[team4]

        events1["name"] = "{} vs {}".format(team_name[team1[1:]],team_name[team2])
        events2["name"] = "{} vs {}".format(team_name[team3[1:]],team_name[team4])

        res.append(events1)
        res.append(events2)
        i+=2
    except:
        break

# res = json.dumps(res, ensure_ascii=False, indent="\t")
with open('events.json','w',encoding="utf-8") as make_file:
    json.dump(res, make_file, ensure_ascii=False, indent="\t")