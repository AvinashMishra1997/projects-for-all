
def histogram(l):

    newlist1 = list()
    newlist= list()
    for a in range(len(l)):
        counter = 0
        if l[a] not in newlist1:
            newlist1.append(l[a])
            for b in l[a:]:

                if b == l[a]:
                    counter+=1
            newlist.append((l[a],counter))
    for x in range(len(newlist)-1,0,-1):
        for y in range(x):
            if newlist[y][1] > newlist[y+1][1]:
                temp = newlist[y]
                newlist[y]=newlist[y+1]
                newlist[y+1]=temp


    for x in range(len(newlist)-1,0,-1):
        for y in range(x):
            if newlist[y][1] == newlist[y+1][1] and newlist[y] > newlist[y+1]:
                temp = newlist[y]
                newlist[y]=newlist[y+1]
                newlist[y+1]=temp
    print(newlist)

