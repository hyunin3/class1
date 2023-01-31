a = 10
b = int(input())

if b == 0:
    print('something wrong')
else:
    print(a/b)    
#에러가 날 만한 상황들을 고려해야
try:
    print('calculating') #바로 except로 넘어가는게 아님
    print(a/b)
except:
    print('something wrong')    

try:
    1/0
except Exception as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
    print('wrong')   
except TypeError as e:
    print(e)
    print('wrong')    
else:
    print('work')
finally:
    print('it works')        