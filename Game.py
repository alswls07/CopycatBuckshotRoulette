import random

round=1
turn=True
gun=[]
dealer_life=0
user_life=0

def start(): # 게임 시작
    global round
    if round==1:
        round_1()
#    elif round==2:
#       round_2()
#    elif round==3:
#        round_3()
    print('test')

def game(r, d):
    global turn
    global dealer_life
    global user_life
    dealer_item=[0 for i in range(8)]
    user_item=[0 for i in range(8)]
    i=0
    while i<4: # dealer_life>0 or user_life>0 or r>0 턴 끝나는 조건
        if turn==True:
            print('- 플레이어의 차례 -')
            while turn==True:
                choice=int(input())
                if choice>=1 and choice<=8: # 아이템 사용
                    if user_item[choice+1]!=0: 
                        item(choice)
                        user_item[choice+1]-=1
                    else:
                        continue
                else: # 총쏘기
                    pass
                turn=False
        else:
            print('- 딜러의 차례 -')
            turn=True
            i+=1

def info(r, d): # 탄 정보
    print("실탄 {0}개, 더미탄 {1}개".format(r, d))

def reload(r, d): # 재장전
    s=r+d
    global gun
    gun=[1]*r+[0]*(s-r)
    random.shuffle(gun)

def item(item):
    if item==1: # 수갑
        pass
    elif item==2: # 맥주
        pass
    elif item==3: # 돋보기
        pass
    elif item==4: # 담배
        pass
    elif item==5: # 톱
        pass
    elif item==6: # 대포폰
        pass
    elif item==7: # 인버터
        pass
    else: # 아드레날린
        pass

def round_1():
    global dealer_life
    global user_life
    dealer_life=2
    user_life=2
    def first():
        rbullet=1
        dbullet=2
        info(rbullet, dbullet)              
        reload(rbullet, dbullet)
        game(rbullet, dbullet)
    def second():
        rbullet=3
        dbullet=2
        info(rbullet, dbullet)              
        reload(rbullet, dbullet)
        game(rbullet, dbullet)
    first()
    second()


# def round_2():
#     dealer_life=4
#     user_life=4

# def round_3():
#     dealer_life=4
#     user_life=4
#     dealer_rlife=2
#     user_rlife=2

print('--------------------- Buckshot Roulette ---------------------')
print('아이템이 있을 시 아이템을 쓰려면 번호에 맞게 누르십시오.')
print('9를 눌러 딜러를 쏠 수 있고 0을 눌러 자신을 쏠 수 있습니다.')
print('-------------------------------------------------------------')
input('게임을 시작하려면 아무 키를 누르세요.')
start()