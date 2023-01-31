test_list = [1,2,3,7,5,4,6]
test_list.sort()
print(test_list)


def check(x):
    return x[1]

scores = [('eng', 88), ('sci', 90), ('math', 80)]
#정렬
print(scores)
scores.sort()
print(scores) #맨 앞에 있는 과목명 기준으로 정렬됨
#뒤의 점수 정렬하려면
scores.sort(key = check) #def로 함수 만들어서 넣어주거나
scores.sort(key = lambda x: x[1]) #람다 쓰거나
print(scores)