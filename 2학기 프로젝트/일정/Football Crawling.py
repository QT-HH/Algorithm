import json
import sys
sys.stdin = open('inputFoot.txt', 'rt', encoding='UTF8')

team = {}
teams = ["강원","광주","대구","서울","성남","수원","수원FC","울산","인천","전북","제주","포항"]
for i in range(1,13):
    team[teams[i-1]] = i

# for i in range(1,13):
#     team[i] = teams[i-1]

print(team)

res = []

i = 806
while True:
    try:
        x = input()
        event = {}
        # print(x[:4])
        if x[:4] == "2021":
            day = x[:10].replace(".","-")
            input()

        team1, time, team2 = input().split()
        input()
        event["id"] = i
        i+=1
        event["events_no"] = 1
        event["start"] = day
        event["start_time"] = time
        event["team1_id"] = team[team1]
        event["team2_id"] = team[team2]
        event["name"] = "{} vs {}".format(team1,team2)
        event["team1_score"] = 0
        event["team2_score"] = 0
        event["team1_user"] = []
        event["team2_user"] = []
        event["draw_user"] = []
        event["betDone"] = False
        event["gameDone"] = False

        res.append(event)

    except:
        break

# print(res)
with open('eventsFoot.json', 'w', encoding="utf-8") as make_file:
    json.dump(res, make_file, ensure_ascii=False, indent="\t")
