import random
import time
import lists
import json

import result_logic

total_money = 1000


running = True
while running:
    try:
        bet = int(input("\nhow much would you like to bet?\n"))
    except ValueError:
        print("you bet must be a integer, set bet to 1")
        bet = 1
    if total_money >= bet:
        total_money -= bet
    else:
        print(f"you cannot afford to bet that much. you only have ${total_money}")
        break

    chance = 7
    if bet > 0:
        chosen_spin = result_logic.spin()
        if chosen_spin is False:
            slot_1 = random.randint(0, chance)
            slot_2 = random.randint(0, chance)
            slot_3 = random.randint(0, chance)
        elif chosen_spin:
            slot_1 = chosen_spin
            slot_2 = chosen_spin
            slot_3 = chosen_spin
        else:
            pass

        for i in range(random.randint(10, 25)):
            print(f"\r{lists.options[random.randint(0, 7)]} | {lists.options[random.randint(0, 7)]} | {lists.options[random.randint(0, 7)]}", end='', flush=True)
            time.sleep(0.1)
        for i in range(random.randint(10, 25)):
            print(f"\r{lists.options[slot_1]} | {lists.options[random.randint(0, 7)]} | {lists.options[random.randint(0, 7)]}", end='', flush=True)
            time.sleep(0.1)
        for i in range(random.randint(10, 25)):
            print(f"\r{lists.options[slot_1]} | {lists.options[slot_2]} | {lists.options[random.randint(0, 7)]}", end='', flush=True)
            time.sleep(0.1)
        print(f"\r{lists.options[slot_1]} | {lists.options[slot_2]} | {lists.options[slot_3]}\n", end='', flush=True)
        result_str = str(slot_1)
        result_str += str(slot_2)
        result_str += str(slot_3)
        if slot_1 == slot_2 == slot_3:
            with open("results.json") as file:
                data = json.load(file)

            if result_str in data:
                print(data[result_str])
                winnings = bet * data[result_str]
                print(f"you win ${winnings}")
                total_money += winnings
                print(f"current balance: ${total_money}")
        elif result_str.count("0") == 2:
            winnings = bet * 3
            print(f"you win ${winnings}")
            total_money += winnings
            print(f"current balance: ${total_money}")
        elif result_str.count("0") == 1:
            winnings = bet * 2
            print(f"you win ${winnings}")
            total_money += winnings
            print(f"current balance: ${total_money}")
        else:
            print("you lose...")
            print(f"current balance: ${total_money}")
    elif bet <= 0:
        print("Your bet must be a positive integer")




