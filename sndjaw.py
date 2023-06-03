
while True:
    answer = input('낼것(가위, 바위, 보)를 입력하세요 :')
    second_answer = input('두번쨰 낼것(가위, 바위, 보)를 입력하세요 :')

    if second_answer == answer:
        print("무승부")
    elif second_answer == '가위' and answer == '바위':
        print("1번 승리")
    elif second_answer == '가위' and answer == '보':
        print("2번 승리")
    elif second_answer == '바위' and answer == '가위':
        print("2번 승리")
    elif second_answer == '바위' and answer == '보':
        print("1번 승리")
    elif second_answer == '보' and answer == '바위':
        print("2번 승리")    
    elif second_answer == '보' and answer == '가위':
        print("1번 승리")
        break
        
