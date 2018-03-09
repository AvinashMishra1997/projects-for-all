def transcript(coursedetails,studentdetails,grades):
    list=[]
    rawresult=[]
    result=[]
    if(len(coursedetails[0])==0 or len(coursedetails[1])==0 or len(studentdetails[0])==0 or len(studentdetails[1])==0 or len(grades[0])==0 or len(grades[1])==0 or len(grades[2])==0):
        exit()
    else:
        for g in grades:
            for c in coursedetails:
                if g[1]==c[0]:
                    course=c[1]
                    list.append((g[0],g[1],course,g[2]))
        for x in range(len(list) - 1, 0, -1):
            for y in range(x):
                if list[y][0] > list[y + 1][0]:
                    temp = list[y]
                    list[y] = list[y + 1]
                    list[y + 1] = temp
        for g in grades:
            for s in studentdetails:
                if g[0]==s[0]:
                    student=s[1]
                    for c in list:
                        if g[0]==c[0]:
                            rawresult.append(c[1:])
                    result.append((g[0],student,rawresult))
                    rawresult=[]
        result=result[:len(studentdetails)]
        for x in range(len(result) - 1, 0, -1):
            for y in range(x):
                if result[y][0] > result[y + 1][0]:
                    temp = result[y]
                    result[y] = result[y + 1]
                    result[y + 1] = temp
        for x in range(len(result)):
            for y in range(len(result[x][2]) - 1, 0, -1):
                for z in range(y):
                    if result[x][2][z] > result[x][2][z+1]:
                        temp = result[x][2][z]
                        result[x][2][z] = result[x][2][z+1]
                        result[x][2][z+1] = temp
        print(result)