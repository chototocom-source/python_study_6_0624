그린컴퓨터파이썬훈련={}

그린컴퓨터파이썬훈련['훈련명'] = '파이썬시각화'
그린컴퓨터파이썬훈련['시간'] = '오후 7시'
그린컴퓨터파이썬훈련['훈련명'] = '파이썬기초 훈련 및 시각화'


print(그린컴퓨터파이썬훈련)

combined_data = {}

for key, value in 그린컴퓨터파이썬훈련.items():
    combined_data[key] = value

print(f"{combined_data}: 확인")


# 선언 예시
user_profile = {
    "name": "홍길동",
    "age": 30,
    "skills": ["Python", "Web"]
}

# 조회 예시
print(user_profile["name"])  # 출력: 홍길동

# Ex. Home이라는 key에 신도림이라는 value을 넣어주세요.
user_profile['Home'] = '신도림'
print(user_profile)
# Ex. age 값을 40으로 수정
user_profile['age'] += 10
print(user_profile)
# Ex. Skill에 App추가해주세요.
user_profile['skills'].append('App')  # user_profile['skills'][2] = 'App' -> 이것도 가능
print(user_profile)

# for, range문 사용
for i in range(1, 50 + 1):
    if i % 2 == 0:
        print(i)