import json
import sys
sys.stdin = open('inputLOL.txt', 'rt', encoding='UTF8')

team = {}

teams = ["담원 기아","DRX","젠지e스포츠","아프리카 프릭스","T1","kt 롤스터","리브 샌드박스","농심 레드포스","한화생명e스포츠","프레딧 브리온"]
for i in range(33,43):
    team[teams[i-33]] = i

# for i in range(33,42):
#     team[i] = teams[i-32]
# print(team)
print(team)
res = []

i = 1
while True:
    try:
        event1 = {}
        event2 = {}

        event1["id"] = i
        event2["id"] = i+1
        i+=2

        sch = input()[1:]
        sch, x = sch.split("(")
        m,d = sch.split("월")
        if len(m) == 1:
            m = '0'+m
        sch = "2021-{}-{}".format(m,d[:-1])
        event1["start"] = sch
        event2["start"] = sch
        event1["start_time"] = "17:00"
        event2["start_time"] = "20:00"

        input()
        team1,team2 = input().split("-")
        team3,team4 = input().split("-")
        event1["team1_id"] = team[team1[1:]]
        event1["team2_id"] = team[team2]
        event2["team1_id"] = team[team3[1:]]
        event2["team2_id"] = team[team4]

        event1["name"] = "{} vs {}".format(team1[1:],team2)
        event2["name"] = "{} vs {}".format(team3[1:],team4)

        event1["team1_score"] = 0
        event1["team2_score"] = 0
        event2["team1_score"] = 0
        event2["team2_score"] = 0

        event1["events_no"] = 3
        event2["events_no"] = 3

        event1["team1_user"] = []
        event1["team2_user"] = []
        event1["draw_user"] = []
        event1["betDone"] = False
        event1["gameDone"] = False

        event2["team1_user"] = []
        event2["team2_user"] = []
        event2["draw_user"] = []
        event2["betDone"] = False
        event2["gameDone"] = False

        res.append(event1)
        res.append(event2)

    except:
        break



with open('eventsLOL.json', 'w', encoding="utf-8") as make_file:
    json.dump(res, make_file, ensure_ascii=False, indent="\t")