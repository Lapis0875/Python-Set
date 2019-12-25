array1: list = [1, 2, 3, 4, 5]
array2: list = [1, 1, 2, 2, 3, 4, 5]
set1: set = set(array1)
set2: set = set(array2)

# 사용자가 두 집합에 값을 입력하도록 합니다.
print('1번 집합의 원소들을 입력해주세요. 반드시 정수를 입력해주셔야 합니다. : ')
count1: int = 0
input1: bool = True
while input1:
    try:
        num = int(input(f'1번 집합의 {count1}번째 원소를 입력해주세요 : '))
    except TypeError:
        print('잘못된 원소를 입력하셨습니다! 다시 입력해 주세요.')
        continue
    count1 += 1