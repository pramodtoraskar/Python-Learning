
g_v = 1


# Uses global because there is no local 'g_v'
def f_1():
    print('Inside f_1() : ', g_v)


# Variable 'G_V' is redefined as a local
def f_2():
    g_v = 2
    print('Inside f_2() : ', g_v)


# Uses global keyword to modify global 'g_v'
def f_3():
    global g_v
    g_v = 3
    print('Inside h() : ', g_v)


# Global scope
print('global variable: ', g_v)
f_1()

print('global variable : ', g_v)
f_2()

print('global variable : ', g_v)
f_3()
print('global variable : ', g_v)