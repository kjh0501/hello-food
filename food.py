# 음식 리스트 중에서 
# 그 중 하나를 추천

foodlist= ["짜장면","짬뽕","탕슛","돈까스","우동"]

import random
#print(foodlist[2])
#그 중 하나를 추천
food=random.choice(foodlist)
print(food)
#5번을 연속으로 추천해보자
for i in range(5):
    # print(i+1)
    food=random.choice(foodlist)
    print(f"{i+1}"."{food}")
    print("1.짜장면")
    
    
    print("종료")
    