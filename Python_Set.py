# 변수 선언 : 
# set1, set2 : 각각 array1, array2를 집합으로 바꿔서 저장함.
set1: set = set()
set2: set = set()


def get_input(mode: int):
    global set1, set2

    # array1, array2 : 입력을 저장할 list
    array1: list = []
    array2: list = []

    if mode == 1:
        # 사용자가 두 집합에 값을 원소 하나씩 입력하도록 함.

        # 1번 집합 원소 입력
        print('1번 집합의 원소들을 입력해주세요. 반드시 정수를 입력해주셔야 합니다. : ')
        count1: int = 1  # 1번 집합 원소를 추가하는 while문의 반복 횟수 측정

        while True:
            try:
                num = int(input(f'1번 집합의 {count1}번째 원소를 입력해주세요 : '))
            except:
                print('잘못된 원소를 입력하셨습니다! 다시 입력해 주세요.')
                continue
            array1.append(num)
            count1 += 1
            answer = input('계속 입력하시겠습니까? Y/N : ')
            if answer == 'Y':
                print('Y 를 입력하셨습니다. 1번 배열의 입력을 계속합니다.')
                continue
            elif answer == 'N':
                print('N 을 입력하셨습니다. 1번 배열의 입력을 종료합니다.')
                break
            else:
                print('잘못된 대답입니다. 1번 배열의 입력을 종료합니다.')
                break
        set1 = set(array1)

        # 2번 집합 원소 입력
        print('2번 집합의 원소들을 입력해주세요. 반드시 정수를 입력해주셔야 합니다. : ')
        count2: int = 1  # 2번 집합 원소를 추가하는 while문의 반복 횟수 측정

        while True:
            try:
                num = int(input(f'2번 집합의 {count2}번째 원소를 입력해주세요 : '))
            except:
                print('잘못된 원소를 입력하셨습니다! 다시 입력해 주세요.')
                continue
            array2.append(num)
            count2 += 1
            answer = input('계속 입력하시겠습니까? Y/N : ')
            if answer == 'Y':
                print('Y 를 입력하셨습니다. 1번 배열의 입력을 계속합니다.')
                continue
            elif answer == 'N':
                print('N 을 입력하셨습니다. 1번 배열의 입력을 종료합니다.')
                break
            else:
                print('잘못된 대답입니다. 1번 배열의 입력을 종료합니다.')
                break
        set2 = set(array2)
    if mode == 2:
        print('각 집합의 원소들을 `1,2,3,4,5` 와 같은 형태로 입력해 주세요.')
        nums = input('1번 집합의 원소들을 입력해 주세요 : ')
        array1_str = nums.translate(str.maketrans('', '', ' ')).split(',')
        try:
            for num_str in array1_str:
                array1.append(int(num_str))
        except:
            print('잘못된 입력입니다! 프로그램을 종료합니다.')
            exit(-2)
        set1 = set(array1)
        nums = input('2번 집합의 원소들을 입력해 주세요 : ')
        array2_str = nums.translate(str.maketrans('', '', ' ')).split(',')
        try:
            for num_str in array2_str:
                array2.append(int(num_str))
        except:
            print('잘못된 입력입니다! 프로그램을 종료합니다.')
            exit(-3)
        set2 = set(array2)


# 프로그램 시작시 안내문
print('='*35)
print('집합 연산 프로그램을 이용해 주셔서 감사합니다.\n안내사항을 따라 두 집합의 원소들을 입력해 주시고, 연산을 수행해 주세요.')
print('제작자 : 2019학년도 영훈고등학교 1학년 3반 4번 김민준 학생.')
print('이 프로그램은 "Python" 이라는 프로그래밍 언어로 개발되었습니다.')
print('='*35)

# 입력모드 : 0일시 안전입력 (반복문 돌며 일일히 입력) / 1일시 편리한 입력 (' , ' 로 구분지은 정수 여러개 한꺼번에 입력)
print('입력 모드는 두가지가 있습니다.')
print('1. 원소 한개씩 입력하기 <-- 안전하지만, 느립니다.')
print('2. 집합 원소 한번에 입력하기 <-- 빠르고 편리하지만, 오류가 날 가능성이 있습니다.')

try:
    input_mode = int(input('입력 모드를 설정해주세요 : '))
except:
    print('잘못된 입력입니다! 프로그램을 종료합니다.')
    exit(-1)
get_input(input_mode)

# 입력한 집합 확인
print('입력하신 두 집합을 확인합니다.')
print(f'1번 집합 : \n {set1} \n 원소 개수 : {len(set1)}')
print(f'2번 집합 : \n {set2} \n 원소 개수 : {len(set2)}')

# 선택한 연산 수행
while True:
    # 수행할 연산 선택
    print('입력하신 두개의 집합들로 연산을 진행하겠습니다. 다음 중 원하시는 연산을 선택해주세요.')
    print('1. 합집합 | 2. 교집합')
    print('3. 차집합 (1번 - 2번) | 4. 차집합 (2번 - 1번) | 5. 대칭차집합')
    print('6. 부분집합 여부 확인 | 7. 교집합 존재여부 확인')

    # 선택한 연산 수행
    answer = input('원하시는 연산의 번호를 입력해주세요 : ')
    if answer == '1':
        print('1번 집합과 2번 집합의 합집합을 구합니다.')
        print(set1 | set2)
    elif answer == '2':
        print('1번 집합과 2번 집합의 교집합을 구합니다.')
        print(set1 & set2)
    elif answer == '3':
        print('1번 집합에서 2번 집합을 뺀 차집합을 구합니다.')
        print(set1 - set2)
    elif answer == '4':
        print('2번 집합에서 1번 집합을 뺀 차집합을 구합니다.')
        print(set2 - set1)
    elif answer == '5':
        print('1번 집합과 2번 집합의 대칭차집합을 구합니다.')
        print(set1^set2)
    elif answer == '6':
        print('1번 집합과 2번 집합의 부분집합 여부를 구합니다.')
        print(f'1번 집합은 2번 집합의 부분집합이다? > {set1.issubset(set2)}')
        print(f'1번 집합은 2번 집합을 포함한다? > {set1.issuperset(set2)}')
        print(f'2번 집합은 1번 집합의 부분집합이다? > {set2.issubset(set1)}')
        print(f'2번 집합은 1번 집합을 포함한다? > {set2.issuperset(set1)}')
    elif answer == '7':
        print('1번 집합과 2번 집합의 교집합의 존재 여부를 구합니다.')
        result = not set1.isdisjoint(set2) and not set2.isdisjoint(set1)
        print(result)
    else:
        print('잘못된 입력입니다. 다시 선택해주세요.')
        continue

    answer = input('연산을 계속하시겠습니까? Y/N : ')
    if answer == 'Y':
        print('Y 를 입력하셨습니다. 연산을 계속하겠습니다.')
        continue
    elif answer == 'N':
        print('N 을 입력하셨습니다. 연산을 종료하겠습니다.')
        break
    else:
        print('잘못된 입력입니다. 연산을 종료하겠습니다.')
        break

# 모든 작업 수행 완료. 프로그램 종료.
print('프로그램을 종료합니다.')


