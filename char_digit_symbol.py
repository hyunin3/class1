#주어진 문자열에서 숫자, 문자, 기호가 
#각각 몇개인지를 출력하는 함수 작성
def check(input_str):
    char_cnt = 0
    digit_cnt = 0
    symbol_cnt = 0
    
    for char in input_str:
        if char.isalpha():
            char_cnt =  char_cnt + 1
        elif char.isdigit():
            digit_cnt = digit_cnt + 1
        else:
            symbol_cnt = symbol_cnt + 1       
    return char_cnt, digit_cnt, symbol_cnt         

input_str = '123#$!asd_snow'
rlt = check(input_str)
print(rlt)
char_cnt, digit_cnt, symbol_cnt = check(input_str)
print(f'char: {char_cnt}, digit: {digit_cnt}, symbol: {symbol_cnt}')