# 문제 설명
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

#     1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
#     2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
#     3. 2에서 나온 배열의 3번째 숫자는 5입니다.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
#     array의 길이는 1 이상 100 이하입니다.
#     array의 각 원소는 1 이상 100 이하입니다.
#     commands의 길이는 1 이상 50 이하입니다.
#     commands의 각 원소는 길이가 3입니다.

# 입출력 예
# array
# [1, 5, 2, 6, 3, 7, 4]
# commands
# [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# return
# [5, 6, 3]


# 나의 풀이
def solution(array, commands):
    answer = []
    
    for i in commands:
        ary = array[i[0]-1:i[1]] # 문제에 주어진 크기만큼 자르기
        ary.sort() # sort 함수로 정렬
        answer.append(ary[i[2]-1]) # k번째 값 answer 리스트 저장
        
    return answer



# 가장 짧은 코드
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# 문법 설명
# # map 과 lambda 함수
# - map(함수, 리스트) 여러 개의 데이터를 한번에 다른 형태로 변환하기 위해서 사용됩니다.
# - lambda 인자 : 표현식

# ls = ['1','2','3']
# list(map(int, ls))
# [1, 2, 3]

# set(map(lambda x: x ** 2, range(5)))
# {0, 1, 4, 9, 16}​


