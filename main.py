import random

name = input("캐릭터 이름을 정하시오 :")

level = 10
level_up = 0
hp_max= 100
hp = hp_max
attack = 10
difficulty = 5
print("=======캐릭터 정보=======")
print("캐릭터 이름 : ", name)
print("레벨 : ", level)
print("체력 : ", hp)
print("공격력 : ", attack)
monster_name = ["슬라임", "고블린", "드래곤"]
monster_hp = [30, 60, 200]
monster_attack = [5, 10, 50]
monster_index = 0
action = ""

def show_monster_info(name, hp, attack):
    print("몬스터 :", name)
    print("몬스터 체력 :", hp)
    print("몬스터 공격력 :", attack)
def show_character_info(level,hp,hp_max,attack,level_up):
    print("레벨 : ", level)
    print("체력 : ", hp , "/", hp_max)
    print("공격력 : ", attack)
    print("경험치 : ", level_up)
def get_action():
    while True:
        action = input("행동을 선택하세요. (1. 공격 2. 도망) : ")
        if action == "1" or action == "공격":
            return "공격"
        elif action == "2" or action == "도망":
            return "도망"
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

while True:
    if hp <= 0:
        print("캐릭터가 사망하였습니다. 게임을 종료합니다.")
        break
    if difficulty == 5 or monster_hp[monster_index] <= 0:
        print("----------------------------------")
        print("난이도를 선택하세요.")
        print("1. 쉬움 2. 보통 3. 어려움 0. 종료")
        difficulty = input("난이도 선택 : ")
        if difficulty == "1" or difficulty == "쉬움":
            monster_index = 0
        elif difficulty == "2" or difficulty == "보통":
            monster_index = 1
        elif difficulty == "3" or difficulty == "어려움":
            monster_index = 2
        elif difficulty == "0" or difficulty == "종료":
            print("게임을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")
            continue
    if monster_hp[monster_index] <= 0:
        monster_hp = [30, 60, 200]
    show_monster_info(monster_name[monster_index], monster_hp[monster_index], monster_attack[monster_index])

    if hp >= 1 and monster_hp[monster_index] >= 1:
        print("----------------------------------")
        action = get_action()
        print("----------------------------------")
        if action == "공격":
            player_damage = random.randint(attack - 3, attack + 3)
            monster_damage = random.randint(monster_attack[monster_index] - 2,monster_attack[monster_index] + 2)
            hp = max(0, hp - monster_damage)
            monster_hp[monster_index] = max(0, monster_hp[monster_index] - player_damage)
            print("몬스터에게 ", player_damage, "의 피해를 입혔습니다.")
            print("몬스터에게 ", monster_damage, "의 피해를 입었습니다.")
            print("현재 체력 : ", hp)
            if monster_hp[monster_index] <= 0:
                print("몬스터를 처치하였습니다.")
                hp = min(hp_max, hp + 40)
                print("----------------------------------")
                print("체력이 40 회복되었습니다. 현재 체력 : ", hp)
                level_up += 10
                if level_up >= level:
                    level += 1
                    hp_max += 10
                    attack += 5
                    level_up = 0
                    print("레벨업! 현재 레벨 : ", level)
                print("레벨업 경험치 10을 획득하였습니다. 현재 레벨업 경험치 : ", level_up)
                print("----------------------------------")
                show_character_info(level, hp, hp_max, attack, level_up)
        elif action == "도망":
            print("도망쳤습니다.")
            difficulty = 5
            continue
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

   

    
    
    