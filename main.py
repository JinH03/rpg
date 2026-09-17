import random
import json
import os



level = 10
level_up = 0
hp_max= 100
hp = hp_max
attack = 10
difficulty = 5
user_gold = 0
monsters =[
    {"name": "슬라임", "hp": 30, "max_hp": 30, "attack": 5 , "exp": 10, "gold": 30},
    {"name": "고블린", "hp": 60, "max_hp": 60, "attack": 10, "exp": 20, "gold": 50},
    {"name": "드래곤", "hp": 200, "max_hp": 200, "attack": 20, "exp": 100, "gold": 200}
]
monster_index = 0
action = ""
inventory = {"체력 회복 물약": 0, "공격력 강화 물약": 0}
def save_game(name, level, level_up,hp, hp_max, attack, gold, inventory):
    game_data = {
        "name": name,
        "level": level,
        "level_up": level_up,
        "hp": hp,
        "hp_max": hp_max,
        "attack": attack,
        "gold": gold,
        "inventory": inventory
    }
    with open("game_save.json", "w", encoding="utf-8") as save_file:
        json.dump(game_data, save_file, ensure_ascii=False, indent=2)
    print("게임이 저장되었습니다.")
def load_game():
    if os.path.exists("game_save.json"):
        with open("game_save.json", "r", encoding="utf-8") as save_file:
            game_data = json.load(save_file)
        return game_data
    return None

def show_monster_info(monster):
    print("몬스터 :", monster["name"])
    print("몬스터 체력 :", monster["hp"], "/", monster["max_hp"])
    print("몬스터 공격력 :", monster["attack"])
def show_character_info(level,hp,hp_max,attack,level_up,user_gold):
    print("레벨 : ", level)
    print("체력 : ", hp , "/", hp_max)
    print("공격력 : ", attack)
    print("경험치 : ", level_up)
    print("골드 : ", user_gold)
def get_action():
    while True:
        action = input("행동을 선택하세요. (1. 공격 2. 포션 사용 3. 도망) : ")
        if action == "1" or action == "공격":
            return "공격"
        elif action == "2" or action == "포션 사용":
            return "포션 사용"
        elif action == "3" or action == "도망":
            return "도망"
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")
def select_monster():
    while True:
        print("----------------------------------")
        print("난이도를 선택하세요.")
        print("1. 쉬움 2. 보통 3. 어려움 4. 상점 0. 저장 및 종료" )
        print("----------------------------------")
        choice = input("난이도 선택 : ")

        if choice == "1" or choice == "쉬움":
            return 0
        elif choice == "2" or choice == "보통":
            return 1
        elif choice == "3" or choice == "어려움":
            return 2
        elif choice == "4" or choice == "상점":
            return "shop"
        elif choice == "0" or choice == "종료" or choice == "저장":
            return "save"
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")
def select_game_mode():
    while True:
        print("게임 모드를 선택하세요.")
        print("1. 새 게임 2. 불러오기")
        choice = input("선택 : ")
        if choice == "1" or choice == "새 게임":
            return "new"
        elif choice == "2" or choice == "불러오기":
            return "load"
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")
def shop(user_gold, inventory):
    while True:
        print("=======상점=======")
        print("현재 골드 : ", user_gold)
        print("1. 체력 회복 (50골드) 2. 공격력 강화 (100골드) 3. 나가기")
        choice = input("선택 : ")
        if choice == "1":
            if user_gold >= 50:
                user_gold -= 50
                inventory["체력 회복 물약"] += 1
                print("체력 회복 물약을 구매하였습니다")
                print("남은 체력 회복 물약 : ", inventory["체력 회복 물약"])
                print("현재 골드 : ", user_gold)
            else:
                print("골드가 부족합니다.")
        elif choice == "2":
            if user_gold >= 100:
                user_gold -= 100
                inventory["공격력 강화 물약"] += 1
                print("공격력 강화 물약을 구매하였습니다.")
                print("남은 공격력 강화 물약 : ", inventory["공격력 강화 물약"])
                print("현재 골드 : ", user_gold)
            else:
                print("골드가 부족합니다.")
        elif choice == "3":
            return user_gold, inventory
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")
def monster_counter(monster):
    if random.random() < 0.1:
        print("몬스터가 카운터를 성공했습니다!")
        return monster["attack"] * 2
    else:
        print("몬스터가 카운터를 시도했지만 실패했습니다.")
        return 0
def use_potion(inventory, potion_type):
    if potion_type == "체력 회복 물약":
        if inventory[potion_type] > 0:
            inventory[potion_type] -= 1
            return 50
        else:
            print("체력 회복 물약이 없습니다.")
            return 0
    elif potion_type == "공격력 강화 물약":
        if inventory[potion_type] > 0:
            inventory[potion_type] -= 1
            return 5
        else:
            print("공격력 강화 물약이 없습니다.")
            return 0
    
game_mode = select_game_mode()
if game_mode == "new":
    print("새 게임을 시작합니다.")
    name = input("캐릭터 이름을 정하시오 :")
elif game_mode == "load":
    loaded_data = load_game()
    if loaded_data:
        name = loaded_data["name"]
        level = loaded_data["level"]
        level_up = loaded_data["level_up"]
        hp = loaded_data["hp"]
        hp_max = loaded_data["hp_max"]
        attack = loaded_data["attack"]
        user_gold = loaded_data["gold"]
        inventory = loaded_data.get("inventory",{"체력 회복 물약": 0, "공격력 강화 물약": 0})
        print("게임을 불러왔습니다.")
    else:
        print("저장된 게임이 없습니다. 새 게임을 시작합니다.")
        name = input("캐릭터 이름을 정하시오 :")
        
print("=======캐릭터 정보=======")
print("캐릭터 이름 : ", name)
print("레벨 : ", level)
print("체력 : ", hp)
print("공격력 : ", attack)
print("골드 : ", user_gold)

while True:
    
    if hp <= 0:
        print("캐릭터가 사망하였습니다. 게임을 종료합니다.")
        break
    if difficulty == 5 or monsters[monster_index]["hp"] <= 0:
        selected = select_monster()
        if selected == "shop":
            user_gold, inventory = shop(user_gold, inventory)
            difficulty = 5
            continue
        if selected == "save":
            save_game(name, level, level_up, hp, hp_max, attack, user_gold, inventory)
            print("게임을 종료합니다")
            break
        monster_index = selected
        difficulty = 0
    if monsters[monster_index]["hp"] <= 0:
        monsters[monster_index]["hp"] = monsters[monster_index]["max_hp"]
    show_monster_info(monsters[monster_index])

    if hp >= 1 and monsters[monster_index]["hp"] >= 1:
        print("----------------------------------")
        action = get_action()
        print("----------------------------------")
        if action == "공격":
            player_damage = random.randint(attack - 3, attack + 3)
            print("몬스터에게 ", player_damage, "의 피해를 입혔습니다.")
            monsters[monster_index]["hp"] = max(0, monsters[monster_index]["hp"] - player_damage)
            
            if monsters[monster_index]["hp"] == 0:
                print("몬스터를 처치하였습니다.")
                hp = min(hp_max, hp + 40)
                print("----------------------------------")
                print("체력이 40 회복되었습니다. 현재 체력 : ", hp)
                level_up += monsters[monster_index]["exp"]
                user_gold += monsters[monster_index]["gold"]
                print("골드 ", monsters[monster_index]["gold"], "을 획득하였습니다. 현재 골드 : ", user_gold)
                if level_up >= level:
                    level += 1
                    hp_max += 10
                    attack += 5
                    level_up = 0
                    print("레벨업! 현재 레벨 : ", level)
                print("레벨업 경험치", monsters[monster_index]["exp"], "을 획득하였습니다. 현재 레벨업 경험치 : ", level_up)
                print("----------------------------------")
                show_character_info(level, hp, hp_max, attack, level_up, user_gold)
            elif random.random() < 0.35:
                print("몬스터가 카운터를 시도합니다!")
                monster_counter_damage = monster_counter(monsters[monster_index])
                hp = max(0, hp-monster_counter_damage)
                print("몬스터의 카운터로", monster_counter_damage, "의 피해를 입었습니다.")
            else:
                monster_damage = random.randint(monsters[monster_index]["attack"] - 2, monsters[monster_index]["attack"] + 2)
                hp = max(0, hp - monster_damage)
                print("몬스터에게 ", monster_damage, "의 피해를 입었습니다.")
            print("현재 체력 : ", hp)

        elif action == "포션 사용":
            print("포션을 사용합니다.")
            potion_using = 0
            inventory_choice = input("사용할 포션을 선택하세요. (1. 체력 회복 물약 2. 공격력 강화 물약) : ")
            if inventory_choice == "1" or inventory_choice == "체력 회복 물약":
                potion_using = use_potion(inventory, "체력 회복 물약")
            elif inventory_choice == "2" or inventory_choice == "공격력 강화 물약":
                potion_using = use_potion(inventory, "공격력 강화 물약") 
            else:
                print("잘못된 입력입니다. 포션 사용을 취소합니다.")

            if potion_using > 0:
                if inventory_choice == "1" or inventory_choice == "체력 회복 물약":
                    hp = min(hp_max, hp + potion_using)
                    print("체력이 회복되었습니다. 현재 체력 : ", hp)
                    print("남은 체력 회복 물약 : ", inventory["체력 회복 물약"])
                elif inventory_choice =="2" or inventory_choice == "공격력 강화 물약":
                    attack += potion_using
                    print("공격력이 강화되었습니다. 현재 공격력 : ", attack)
                    print("남은 공격력 강화 물약 : ", inventory["공격력 강화 물약"])
            monster_damage = random.randint(monsters[monster_index]["attack"] - 2,monsters[monster_index]["attack"] + 2)
            hp = max(0, hp - monster_damage)
            print("몬스터에게", monster_damage, "의 피해를 입었습니다.")
            
        elif action == "도망":
            print("도망쳤습니다.")
            difficulty = 5
            continue
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

   

    
    
    