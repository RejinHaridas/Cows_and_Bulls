import random
print('''<<<<<<<<  WELCOME TO COWS AND BULLS   >>>>>>>>>>>>>>>
        Instructions:>>>>>
        >>  Guess the 4 digit number
        >>  You will have 5 chances for guessing the number.
        >>  If your guess has the same number as the original number in the rigth position '' 1 bull '' will displayed.
        >>  If your guess has the same number as the original number but in different position  '' 1 cow '' will be displayed.
        >>  zero cannot be used .
        >>  Numbers cannot be repeated
        >> >>>>>>>>>>>>>>>>   ALLL THE BEST   <<<<<<<<<<<<<<<<
        ''')
p=['1','2','3','4','5','6','7','8','9']
random.shuffle(p)
p=p[1::2]
init=(p)
Result=tuple(init)
c='1 cow'
b='1 bull'
ch='Y'
while ch=='Y':
    Count=1
    while Count<=3:
        n=m=0
        t=list(input('enter choice'))
        a=0
        if t is init:
            print('<<<  BOOYAAHHH!!   U WON THE GAME >>>')
            break
        elif '0' in t:
            print('Invalid Choice')
            continue
        while a<4:
            if t[a] in init:
                i=0
                if t[a]==init[a]:
                    n+=1
                else:
                    m+=1
            a+=1
        print(n,'bulls',m,'cows')
        Count+=1
        print()
    if Count>3:
        print('''<<<  SORRY U LOSE!  >>>''')
        print('<< THE ANSWER IS ',Result)
    ch=input('<< TO TRY AGAIN PRESS Y  >>')
