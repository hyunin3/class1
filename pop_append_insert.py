sample_list = [11,22,33,55,66]

#주어진 리스트의 4번째 자리(3번 인덱스)에 있는 항목을 제거하고 변수에 할당하라

print('original_list: ', sample_list)

elem = sample_list.pop(3)

print('list_after: ', sample_list)
print('elem: ',elem)

# sample_list의 가장 뒤에 77을 추가

sample_list.append(77)
print(sample_list)

#할당해놓은 변수의 값을 sample_list의 2번 인덱스에 추가

sample_list.insert(2, elem)
print(sample_list)