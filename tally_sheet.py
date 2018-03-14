from sys import exit

flag=True
result=[]
while flag:
    game_data="exit:"+raw_input()
    if game_data is not "exit:":
        score = game_data.split(":")
        del(score[0])
        score_1 = score[2].split(",")

        for i in range(len(score_1)):
            score_1[i] = score_1[i].split("-")

        score[2] = score_1
        result.append(score)

    else:
        flag=False

name=[]

for i in range(len(result)):
    if result[i][0] not in name:
        name.append(result[i][0])
    if result[i][1] not in name:
        name.append(result[i][1])
t_list=list()
for n in range(len(name)):
    set_5 = 0
    set_3 = 0
    set_won = 0
    game_won=0
    set_lost=0
    game_lost=0
    t_list.append(name[n])
    for i in range(len(result)):
        if (result[i][0]==name[n]) and (len(result[i][2]) > 3 and len(result[i][2]) <= 5):
            set_5+=1
        if (result[i][0]==name[n]) and ((len(result[i][2]) <= 3) and (len(result[i][2]) >1)):
            set_3+=1
        for j in range(len(result[i][2])):

            if (result[i][0]==name[n]) and (result[i][2][j][0] >= result[i][2][j][1]):
                set_won+=1


            if (result[i][0]==name[n]) and (result[i][2][j][0] <= result[i][2][j][1]):
                set_lost+=1


            if (result[i][1]==name[n]) and (result[i][2][j][0] < result[i][2][j][1]):
                set_won+=1

            if (result[i][1]==name[n]) and (result[i][2][j][0] >= result[i][2][j][1]):
                set_lost+=1


            if (result[i][0] == name[n]):
                game_won+=int(result[i][2][j][0])

            if (result[i][1] == name[n]):
                game_won+=int(result[i][2][j][1])

            if (result[i][0] == name[n]):
                game_lost+=int(result[i][2][j][1])

            if (result[i][1] == name[n]):
                game_lost += int(result[i][2][j][0])
    t_list.append(set_5)
    t_list.append(set_3)
    t_list.append(set_won)
    t_list.append(game_won)
    t_list.append(set_lost)
    t_list.append(game_lost)
ll=[]
while(len(t_list)>1):
    ll.append(t_list[:7])
    del(t_list[:7])


for x in range(len(ll) - 1, 0, -1):
    for y in range(x):
        if ll[y][1] < ll[y + 1][1]:
            temp = ll[y]
            ll[y] = ll[y + 1]
            ll[y + 1] = temp

for x in range(len(ll) - 1, 0, -1):
    for y in range(x):
        if (ll[y][1] == ll[y + 1][1]) and (ll[y][2]<ll[y+1][2]):
            temp = ll[y]
            ll[y] = ll[y + 1]
            ll[y + 1] = temp

for x in range(len(ll) - 1, 0, -1):
    for y in range(x):
        if (ll[y][1] == ll[y + 1][1]) and (ll[y][2] == ll[y + 1][2]) and (ll[y][3]<ll[y+1][3]):
            temp = ll[y]
            ll[y] = ll[y + 1]
            ll[y + 1] = temp

for x in range(len(ll) - 1, 0, -1):
    for y in range(x):
        if (ll[y][1] == ll[y + 1][1]) and (ll[y][2] == ll[y + 1][2]) and (ll[y][3]==ll[y+1][3]) and (ll[y][4]<ll[y+1][4]):
            temp = ll[y]
            ll[y] = ll[y + 1]
            ll[y + 1] = temp

for x in range(len(ll) - 1, 0, -1):
    for y in range(x):
        if (ll[y][1] == ll[y + 1][1]) and (ll[y][2] == ll[y + 1][2]) and (ll[y][3]==ll[y+1][3]) and (ll[y][4]==ll[y+1][4]) and (ll[y][6]<ll[y+1][6]):
            temp = ll[y]
            ll[y] = ll[y + 1]
            ll[y + 1] = temp

for x in range(len(ll) - 1, 0, -1):
    for y in range(x):
        if (ll[y][1] == ll[y + 1][1]) and (ll[y][2] == ll[y + 1][2]) and (ll[y][3] == ll[y + 1][3]) and (ll[y][4] == ll[y + 1][4]) and (ll[y][6] == ll[y + 1][6]) and (ll[y][5]<ll[y+1][5]):
            temp = ll[y]
            ll[y] = ll[y + 1]
            ll[y + 1] = temp

for i in range(len(ll)):
    print(ll[i][0],ll[i][1],ll[i][2],ll[i][3],ll[i][4],ll[i][5],ll[i][6])
exit()
