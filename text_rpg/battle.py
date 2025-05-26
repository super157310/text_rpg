import rpg_classes
import game
import os

def battle(your_character, enemy_character):
    # 전투 시작
    print(f"{your_character.name}과(와) {enemy_character.name}의 전투가 시작되었습니다!")
    while True:
        # 플레이어 턴
        print(f"{your_character.name}의 턴입니다.")
        print("1. 공격")
        print("2. 마법")
        print("3. 회복")
        choice = int(input())
        os.system('cls') # 콘솔 화면 지움
        
        if choice == 1:
            your_character.do_attack(enemy_character)
            print(f"당신의 채력: {your_character.health}")
            print(f"{enemy_character.name}의 채력: {enemy_character.health}")  
            if enemy_character.health <= 0:
                print(f"{enemy_character.name}을(를) 처치했습니다!")
                break
        elif choice == 2:
            your_character.do_magic(enemy_character)
            print(f"당신의 채력: {your_character.health}")
            print(f"{enemy_character.name}의 채력: {enemy_character.health}")  
            if enemy_character.health <= 0:
                print(f"{enemy_character.name}을(를) 처치했습니다!")
                break
        elif choice == 3:
            your_character.do_heal()
            print(f"당신의 채력: {your_character.health}")
            print(f"{enemy_character.name}의 채력: {enemy_character.health}")  
        else:
            print("잘못된 선택입니다.")
        
        # 적 턴
        if enemy_character.health > 0:
            print(f"{enemy_character.name}의 턴입니다.")
            enemy_character.do_attack(your_character)
            if your_character.health <= 0:
                print(f"{your_character.name}이(가) 쓰러졌습니다.")
                re=int(input("게임을 다시 시작하시겠습니까? (1: 예, 0: 아니오) "))
                if re == 1:
                    game.main()
                else:
                    print("게임을 종료합니다.")
                    exit()
                    break
                break
    