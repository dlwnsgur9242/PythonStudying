# 파이썬의 사용자 정의 함수(User-Defined Function) 정리


# 사용자 정의 함수(User-Defined Function)
# 형식
# def 함수명(변수명,...):
#     명령어
#     return 반환값

# 소스 코드
def fn(num):
    if num % 2 == 0:
        return 'Y'
    else:
        return 'N'
a = fn(5)
print(a)

# 출력 결과
# N


#추가
# 디폴트 매개변수
# 디폴트 매개변수는 기본값이 정의된 매개변수이다.

# 형식
# def 함수이름(매개변수=디폴트값):
#     명령문