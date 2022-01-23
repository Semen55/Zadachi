from math import fabs
def Dek(usk):
    def S(v1,v2,t):
        a=int(usk(v1,v2,t))
        if a!=-1:
            l=[s,a]
            s=(v1+v2)/2*t
            return l
        else:
            return ''
    return S

@Dek
def usk(v1,v2,t):
    a=int()
    try:
       a=fabs(v1-v2)/(2*t)
    except ZeroDivisionError:
        print('t=0')
        return -1
    except TypeError:
        print('Вы ввели не числа')
        return -1
    else:
        return a





