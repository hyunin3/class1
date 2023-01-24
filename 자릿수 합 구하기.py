s = int(input('숫자를 입력해주세요 : '))

def 자릿수합(s):
    sum=0
    for i in list(str(s)):
        sum=sum+int(i)
    return sum

print(자릿수합(s))