# 중첩 if
x = 15

if x >0:
    print('양수')
    if x > 9:
        print('10보다 큰 수')
    else:
        print('10보다 작은 수')
elif x == 0:
    print('0')
else:
    print('음수')

print()

x = 2
if x != 10: # if문은 항상 참이라고 생각하면 된다. x가 10이 아닌것이 참이다. 
    pass
else:
    pass