words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

for idx in range(1, len(words)):
    print(idx)
    
    if words[idx-1][-1] != words[idx][0]:
        print('실패!', idx, words[idx])
        break

    elif words[idx] in words[:idx]: 
        print('실패!', idx, words[idx])
        break
else:
    print('성공!')