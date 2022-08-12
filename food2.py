import random

foodlist= ["짜장면","짬뽕","탕슛","돈까스","우동"]
#위 리스트를 출력
myfood.print_list(foodlist)
#리스트중에 먹고 싶은 메뉴가 없으면
#사용자가 입력을 한다(계속)
#만약에 그만을 입력하면 입력이 끝나고 
#음식 리스트 출력하고 추천 메뉴가 출력
while true:
    addfood=input("추가 음식 입력:")
    print(f"당신이 입력한 내용:{그만}")  
    #만약에 입력한 글자가 그만과 같다면
    #무한반복을 멈춤
    if addfood=="그만":
        break
    foodlist.append(addfood)
#화면에 음식 리스트를 출력을 하고
for i,food in enumerate(foodlist):
   myfood.print(f"{i+1}.{food}")
    
    # 리스트중에 먹고 싶은 메뉴가 없으면
    # 우리가 추가해서 그중에서 추천 했으면 좋겠다
    addfood=input("김밥:")
    myfood.print(f"당신이 입력한 내용:{addfood}")  
foodlist.append(addfood)
# 음식 리스트 출력
for i,food in enumerate(foodlist):
   print(f"{i+1}.{food}")
