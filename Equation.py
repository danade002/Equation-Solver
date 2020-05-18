#simple simultaneous and quadratic equation solver
print('This system can only solve for simple simultaneous and quadratic equation')
print('\nSimultaneous equation=1'+'\nQuadtratic equation=2')
try:
    selection = int (input('Enter the type of equation you want to solve: '))
    if selection==1:
        A1=int (input('Enter A1: '))
        B1=int (input('Enter B1: '))
        C1=int (input('Enter C1: '))
        A2=int (input('Enter A2: '))
        B2=int (input('Enter B2: '))
        C2=int (input('Enter C2: '))
        numeratorX=((B1*C2)-(B2*C1))
        denominatorX=((A2*B1)-(A1*B2))
        numeratorY=((A1*C2)-(A2*C1))
        denominatorY=((A1*B2)-(A2*B1))
        try: 
            X=numeratorX/denominatorX
            Y=numeratorY/denominatorY
            print ('X= ',X)
            print ('Y= ',Y)
        except ZeroDivisionError:
            print('Cannot be divisible by 0')

    elif selection==2:
        try:
            a= int (input('enter a: '))
            b= int (input('enter b: '))
            c= int (input('enter c: '))
            if (b**2>=4*a*c):
                sq=(b**2-4*a*c)
                import math
                outsq= math.sqrt(sq)
                pend= -b+outsq
                pend1=-b-outsq
                x1=pend/(2*a)
                x2=pend1/(2*a)
                print ('x1=', x1)

                print ('x2=', x2)
            else:
                print('Opps! This calculator does not support complex number')
        except ValueError:
            print ('invalid character, enter an integer')
    else:
        print ('Enter number 1 or 2 for either simulateneous or quadratic equation')
except ValueError:
            print ('invalid character, select either 1 or 2 for the equation you want to solve')
    
