a = "Soojebi 123"
print(a.upper())
print(a.lower())
print(a.isalnum())
print(a.isalpha())
print(a.isdecimal())
print(a.isdigit())
print(a.isspace())
print(a.split())
print(a.split(sep='1'))
str = '1,2,3'.split(",")
print(str)

# 출력
# SOOJEBI 123
# soojebi 123
# False
# False
# False
# False
# False
# ['Soojebi', '123']
# ['Soojebi ', '23']
# ['1', '2', '3']

# 사용한 메서드 정리😽
# upper() 문자열을 대문자로 변환하는 메서드
# lower() 문자열을 소문자로 변환하는 메서드
# isalnum() 문자열이 알파벳 또는 숫자로만 구성되어 있으면 True, 아니면 False를 리턴하는 메서드
# isalpha() 문자열이 알파벳으로만 구성되어 있으면 True, 아니면 False를 리턴하는 메서드
# isdecimal() 문자열이 정수이면 True, 아니면 False를 리턴하는 메서드
# isdigit() 문자열이 숫자이면 True, 아니면 False를 리턴하는 메서드
# isspace() 문자열이 공백으로만 구성되어 있으면 True, 아니면 False를 리턴하는 메서드
# split() 문자열을 매개변수로 전달된 문자(구분자)로 나누어 리스트로 변환하는 메서드