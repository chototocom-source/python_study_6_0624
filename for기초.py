def process_numbers():
    # 1. 반드시 리스트 형 변수를 먼저 선언합니다.
    numbers = ['회사소개', '제품소개', '게시판']
    최종글 = ""
    
    # 2. for문 실행
    for num in numbers:
        # [짝수 판별] 2로 나누어 떨어지면 짝수입니다.
        if num == '제품소개':
            continue  # 아래 코드를 실행하지 않고 다음 숫자로 바로 넘어갑니다.
        
        최종글 = 최종글 + num
            
    return 최종글

# 함수 호출 및 결과 출력
result = process_numbers()    # 함수를 받기 때문에, 함수 내에 'return' 존재
print("최종 반환된 값:", result)