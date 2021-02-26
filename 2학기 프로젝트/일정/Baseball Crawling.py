import json
import sys
sys.stdin = open('inputBase.txt', 'rt', encoding='UTF8')

team = {}
teams = ["두산","롯데","삼성","키움","한화","KIA","KT","LG","NC","SK"]
for i in range(23,33):
    team[teams[i-23]] = i

# for i in range(23,33):
#     team[i] = teams[i-23]

# print(team)
res = []

i = 91
while True:
    try:
        MM,DD = input().split(".")
        for j in range(5):
            events = {}
            events["id"] = i
            i+=1
            events["events_no"] = 2
            events["start"] = "2021-{}-{}".format(MM,DD[:2])
            x, y, z, q = input().split()
            events["start_time"] = x
            team1, team2 = y.split("vs")
            events["team1_id"] = team[team1]
            events["team2_id"] = team[team2]
            events["name"] = "{} vs {}".format(team1,team2)
            events["team1_score"] = 0
            events["team2_score"] = 0
            events["team1_user"] = []
            events["team2_user"] = []
            events["draw_user"] = []
            events["betDone"] = False
            events["gameDone"] = False
            res.append(events)
    except:
        break


with open('eventsBase.json', 'w', encoding="utf-8") as make_file:
    json.dump(res, make_file, ensure_ascii=False, indent="\t")
