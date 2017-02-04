a='   '
b='   '
c='   '
d='   '
e='   '
f='   '
g='   '
h='   '
i='   '

q=print('while entering column number and row number, please do not leave any space in between them \n example (12) or (23), etc')
t=('\t'+a+'|'+b+'|'+c+'\n\t___________\n\t '+d+'|'+e+'|'+f+'\n\t___________\n\t'+g+'|'+h+'|'+i )
print t
for unknowns in t:
    unknowns= raw_input('Enter column number and row number here without spaces in between: ')
    u_s= str(unknowns)
    if u_s == '11':
        a=raw_input('Enter x or o:  ')
    elif u_s == '12':
        b=raw_input('Enter x or o:  ')
    elif u_s == '13':
        c=raw_input('Enter x or o:  ')
    elif u_s == '21':
        d=raw_input('Enter x or o:  ')
    elif u_s == '22':
        e=raw_input('Enter x or o:  ')
    elif u_s== '23':
        f=raw_input('Enter x or o:  ')
    elif u_s == '31':
        g=raw_input('Enter x or o:  ')
    elif u_s == '32':
        h=raw_input('Enter x or o:  ')
    elif u_s == '33':
        i=raw_input('Enter x or o:  ')
    else:
        print ('INPUT ERROR:')
    t1=('\t '+a+' | '+b+' | '+c+' \n\t   ___________\n\t '+d+' | '+e+' | '+f+' \n\t   ___________\n\t '+g+' | '+h+' | '+i )
    t=t1

    print (t)
