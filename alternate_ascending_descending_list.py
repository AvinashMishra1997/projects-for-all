def alternating(l):
    x = 0
    i = 1
    if len(l) >= 3:
        while i in range(len(l)-1):
            if ((l[i]>l[i-1] and l[i]>l[i+1]) or (l[i]<l[i-1] and l[i]<l[i+1])):
                i += 1
            else:
                x = 1
                break

    else:
        x = 0

    if x == 0:
        print("True\n")
    elif x == 1:
        print("False\n")