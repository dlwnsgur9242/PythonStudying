# 문제 설명
#     0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

#     예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

#     0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
#     numbers의 길이는 1 이상 100,000 이하입니다.
#     numbers의 원소는 0 이상 1,000 이하입니다.
#     정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.


# 입출력 예
# numbers
# [6, 10, 2]
# return
# "6210"

# numbers
# [3, 30, 34, 5, 9]
# return
# "9534330"


def solution(numbers):
    # 1. 모든 수를 문자열로 변환
    numbers = list(map(str, numbers))
    # 2. x+y와 y+x를 비교하여 정렬
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    # 3. 정렬된 numbers를 이어붙인 뒤 반환
    return str(int("".join(numbers)))



# 파이썬의 내장 정렬 함수는 **O(N log N)**의 시간 복잡도를 가지기 때문에 효율적으로 동작할 수 있다.
