
def ascending(l):
    x = 0
    i = 1
    j=i-1
    if len(l) >= 2:
        while i in range(len(l)):
            if l[j] <= l[i]:
                x=0
                i += 1
                j = i - 1
            else:
                x=1
                break

    else:
        x=0

    if x==0:
        print("True\n")
    elif x==1:
        print("False\n")

