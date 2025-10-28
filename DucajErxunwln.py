import random
import time
import os
creep_ascii_neutral = r"""
   .-"      "-.
  /            \
 |,  -.-  -.-  ,|
 | )(_o/  \o_)( |
 |/     /\     \|
 (_     ^^     _)
  \__|IIIIII|__/
   | \IIIIII/ |
   \          /
    `--------`
"""
creep_ascii_dead = r"""
   .-"   /
  /      \
 |,  -.- /
 | )(_x/ \
 |/     //
 (_     ^\
  \__|IIII/
   | \III\_____
   \          /
    `--------`
"""
creep_ascii_happy = r"""
   .-"      "-.
  /       .-.  \
 |,  -.-       ,|
 | )(_o/  \o_)( |
 |/     /\     \|
 (_     ^^     _)
  \__|IIIIII|__/
   | \IIIIII/ |
   \          /
    `--------`
"""
creep_ascii_hysterical = r"""
   .-"      "-.
  /            \
 |,   ^    V   ,|
 | )(_+/  \ϴ_)( |
 |/     /\     \|
 (_     ^^     _)
  \_|_______|__/
   | \IIIIII/ |
   \          /
    `--------`
"""
creep_ascii_haughty = r"""
   .-"      "-.
  /            \
 |,      ὢ     ,|
 | ) (=)  (=) ( |
 |/    /||\    \|
 (_     ^^     _)
  \__|IIIIII|__/
   | \IIIIII/ |
   \          /
    `--------`
"""
creep_ascii_squished = r"""
   .-"  "-.
  /        \
 |, -.--.- ,|
 |)(_o/\o_)(|
 |/  /\    \|
 (_  ^^    _)
  \__|III|_/
   | \III/ |
   \       /
    `-----`
"""
creep_ascii_eat = r"""
   .-"      "-.
  /            \
 |,  -.-  -.-  ,|
 | )(_o/  \o_)( |
 |/     /\     \|
 (_     ^^     _)
  \__|IIIIII|__/
   |          |
   | \IIIIII/ |
   \          /
    `--------`
"""
creep_ascii_eat2 = r"""
   .-"      "-.
  /            \
 |,  -.-  -.-  ,|
 | )(_Ὢ/  \Ὢ_)( |
 |/     /\     \|
 (_     ^^     _)
  \__|IIIIII|__/
   |          |
   |          |
   | \IIIIII/ |
   \          /
    `--------`
"""
loading = r"""
--*-------------------------------------
----------------------------------o-----
-------------------o--------------------
------------o---------------------------
--------------------------o-------------
--------------o-------------------------
--o-------------------------------------
-----o----------------------------------
"""
loading2 = r"""
----------------------------------*-----
-------------------o--------------------
------------o---------------------------
--------------------------o-------------
--------------o-------------------------
--o-------------------------------------
-----o----------------------------------
--o-------------------------------------
"""
loading3 = r"""
-------------------*--------------------
------------o---------------------------
--------------------------o-------------
--------------o-------------------------
--o-------------------------------------
-----o----------------------------------
--o-------------------------------------
----------------------------------o-----
"""
loading4 = r"""
------------*---------------------------
--------------------------o-------------
--------------o-------------------------
--o-------------------------------------
-----o----------------------------------
--o-------------------------------------
----------------------------------o-----
-------------------o--------------------
"""
loading5 = r"""
--------------------------*-------------
--------------o-------------------------
--o-------------------------------------
-----o----------------------------------
--o-------------------------------------
----------------------------------o-----
-------------------o--------------------
------------o---------------------------
"""
loading6 = r"""
--------------*-------------------------
--o-------------------------------------
-----o----------------------------------
--o-------------------------------------
----------------------------------o-----
-------------------o--------------------
------------o---------------------------
--------------------------o-------------
"""
loading6 = r"""
--*-------------------------------------
-----o----------------------------------
--o-------------------------------------
----------------------------------o-----
-------------------o--------------------
------------o---------------------------
--------------------------o-------------
--------------o-------------------------
"""
loading7 = r"""
-----*----------------------------------
--o-------------------------------------
----------------------------------o-----
-------------------o--------------------
------------o---------------------------
--------------------------o-------------
--------------o-------------------------
--o-------------------------------------
"""


# --- Game State ---
dice_1 = dice_2 = dice_3 = 0
botdice1 = botdice2 = botdice3 = 0
punishment_number = 0
score = 10
round_num = 1
Punstate = ""
betTimes = 3
big_dice = 0
anim_numb = 0
disable_scary = False
devil = False


def restart_anim():
    global loading, loading2, loading3, loading4, loading5, loading6, loading7
    for i in range(10):
        print(loading)
        time.sleep(0.05)
        clear()
        print(loading2)
        time.sleep(0.05)
        clear()
        print(loading3)
        time.sleep(0.05)
        clear()
        print(loading4)
        time.sleep(0.05)
        clear()
        print(loading5)
        time.sleep(0.05)
        clear()
        print(loading6)
        time.sleep(0.05)
        clear()
        print(loading7)
        time.sleep(0.05)
        clear()


def death_anim():
    global creep_ascii_neutral, creep_ascii_eat, creep_ascii_eat2
    for i in range(5):
        clear()
        print(creep_ascii_eat)
        time.sleep(0.05)
        clear()
        print(creep_ascii_eat2)
        time.sleep(0.5)
        clear()
        print(creep_ascii_neutral)
        time.sleep(0.05)
    print("Tasty")
    time.sleep(1)
    clear()
    print("...")
    time.sleep(1)
    clear()    

def anim():
    global creep_ascii_hysterical, creep_ascii_happy, creep_ascii_haughty, creep_ascii_neutral, creep_ascii_squished, anim_numb
    clear()
    print(creep_ascii_neutral)
    time.sleep(0.5)
    clear()
    anim_numb = random.randint(1,4)
    if anim_numb == 1:
        print(creep_ascii_happy)
    elif anim_numb == 2:
        print(creep_ascii_haughty)
    elif anim_numb == 3:
        print(creep_ascii_hysterical)
    elif anim_numb == 4:
        print(creep_ascii_squished)
    time.sleep(1)

# --- Utility ---
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Punishment Function ---
def punishment():
    global score, response, exp
    exp = random.randint(1,3)
    if exp == 3:
        exp = random.randint(1, 15)
        if exp == 1:
            print("I will savour your flesh")
            response = input("(Type: I will let you) ").lower()
            if response == "i will let you":
                print("Well done")
            else:
                print("...")
                score = 0
        elif exp == 2:
            print("When Will you slip up?")
            response = input("(Type: I don't know) ").lower()
            if response == "i don't know":
                print("Ok I will wait")
            else:
                print("...")
                score = 0
        elif exp == 3:
            print("Will the viewers be happy?")
            response = input("(Type: Yes they will be) ").lower()
            if response == "yes they will be":
                print("After I make a meal out of you")
            else:
                print("...")
                score = 0
        elif exp == 4:
            print("I just love the smell and taste of fear when I gouge out your eyeballs and put them back in")
            response = input("(Type: So do I) ").lower()
            if response == "so do i":
                print("I know you do...")
            else:
                print("...")
                score = 0
        elif exp == 5:
            print("Your organs will be my keepsakes")
            response = input("(Type: Hopefully they will be in perfect condition) ").lower()
            if response == "hopefully they will be in perfect condition":
                print("I will make sure that they will")
            else:
                print("...")
                score = 0
        elif exp == 6:
            print("You know it was nice meeting you...")
            response = input("(Type: Yes you too) ").lower()
            if response == "yes you too":
                print("Thank you but I won't let you go")
            else:
                print("...")
                score = 0
        elif exp == 7:
            print("Keep rolling the dice, I dare you")
            response = input("(Type: Sorry) ").lower()
            if response == "sorry":
                print("...")
            else:
                print("NOOOOOOOOOOOOOOOOOOO")
                score = 0
        elif exp == 8:
            print("When will you know that there is no end")
            response = input("(Type: I already know) ").lower()
            if response == "i already know":
                print("...")
            else:
                print("NOOOOOOOOOOOOOOOOOOO HOW COULD YOU")
                score = 0
        elif exp == 9:
            print("Your head will be quite the taste")
            response = input("(Type: Hopefully it will be in perfect condition) ").lower()
            if response == "hopefully it will be in perfect condition":
                print("I will make sure that it will")
            else:
                print("...")
                score = 0
        elif exp == 10:
            print("My opportunity is your destiny")
            response = input("(Type: Your opportunity is very bright) ").lower()
            if response == "your opportunity is very bright":
                print("I will make sure that they will")
            else:
                print("...")
                score = 0
        elif exp == 11:
            print("Your hair doesn't look tasty, I might as well shave you before my feast")
            response = input("(Type: Please) ").lower()
            if response == "please":
                print("I have a knife that I can use")
            else:
                print("...")
                score = 0
        elif exp == 12:
            print("Your desperate cries will not be sought after")
            response = input("(Type: I am sorry) ").lower()
            if response == "i am sorry":
                print("I am a forgiving person")
            else:
                print("...")
                score = 0
        elif exp == 13:
            print("I WILL CUT YOU LIMB FOR LIMB!!!")
            input("(Type:) ").lower()
            print("Sorry")
        elif exp == 14:
            print("You will always lose you know")
            response = input("(Type: Yes I know) ").lower()
            if response == "yes i know":
                print("You have a very neat plan but it WON'T WORK")
            else:
                print("...")
                score = 0
        elif exp == 15:
            print("I know where you live and will kill your family members")
            input("(Type:) ").lower()
            print("...")
# --- Big Dice Function ---
def bd():
    global score, round_num
    print(f"Round: {round_num}, Score: {score}\n")
    answer = input("Do you want to spin the big die? (Yes/No): ").lower()
    if answer == "yes":
        for _ in range(50):
            clear()
            print(creep_ascii_neutral)
            print(f"Round: {round_num}, Score: {score}\n")
            print("Spinning...")
            print("Side " + str(random.randint(1,6)))
            time.sleep(0.05)
        big_dice = random.randint(1,6)
        if big_dice == 1:
            print("😒 Score + 3")
            score += 3
        elif big_dice == 2:
            print("😒 Round increased by 5")
            round_num += 5
        elif big_dice == 3:
            print("😒 Score + 1")
            score += 1
        elif big_dice == 4:
            print("😒 Jackpot!!! Score + 5")
            score += 5
        elif big_dice == 5:
            print("😀 Unlucky: Score - 1")
            score -= 1
        elif big_dice == 6:
            print("😃 ...Sudden Death! Score = 0")
            score = 0
    else:
        print("Ok then...")

    print(f"Score: {score}\n")
    round_num += 1

# --- Main Game Function ---
def game():
    global score, dice_1, dice_2, dice_3
    global botdice1, botdice2, botdice3
    global Punstate, betTimes, punishment_number, round_num

    print(f"Round: {round_num}, Score: {score}\n")

    # Roll dice
    if Punstate == "LAD":
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        dice_3 = 0
        print(f"Your dice have been rolled {dice_1}, {dice_2}, ₪")
    else:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        dice_3 = random.randint(1, 6)
        botdice1 = random.randint(1, 6)
        botdice2 = random.randint(1, 6)
        botdice3 = random.randint(1, 6)
        if dice_1 + dice_2 + dice_3 == 18:
            print("666")
            devil = True
        if Punstate == "LAE":
            print("Your dice have been rolled x, x, x.")
        else:
            print(f"Your dice have been rolled {dice_1}, {dice_2}, {dice_3}.")

    # IfT9 punishment
    if Punstate == "IfT9" and (dice_1 + dice_2 + dice_3) > 9:
        print("You rolled more than 9! Score -1.")
        score -= 1
        Punstate = ""
    else:
        answer = input("Do you want to bet? (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            Punstate = ""
            player_total = dice_1 + dice_2 + dice_3
            bot_total = botdice1 + botdice2 + botdice3
            if player_total > bot_total:
                print(f"You win! I rolled {botdice1}, {botdice2}, {botdice3}.")
            else:
                print(f"You lose! I rolled {botdice1}, {botdice2}, {botdice3}.")
                score -= 1
                punishment_number = random.randint(1,6)
                if punishment_number == 3:
                    Punstate = "LAD"
                    print("Lose a dice. You can't skip...")
                elif punishment_number == 4:
                    Punstate = "LAE"
                    print("Lose both eyes. You can't skip...")
                elif punishment_number == 5:
                    Punstate = "IfT9"
                    print("If next dice roll > 9, you immediately lose next round. You can't skip...")
        elif answer in ("no", "n"):
            if Punstate in ("LAD", "LAE"):
                score -= 5
                print("You shouldn't have skipped this round...")
                print(score)
                Punstate = ""
                time.sleep(1)
            else:
                if betTimes > 0:
                    betTimes -= 1
                    print(f"You can only decline {betTimes} more time(s).")
                else:
                    score -= 3
                    betTimes = 3
                    print("Score -3 (decline limit reset).")
        elif (answer in ("yes", "y")) and (answer in ("no", "n")):
            score = 0
            print("Invalid input. Answer with 'yes' or 'no'.")
        else:
            score = 0
            print("Invalid input. Answer with 'yes' or 'no'.")
            time.sleep(1)
    print(f"Score: {score}\n")
    round_num += 1

# --- Start Game ---
clear()
while True:
    while True:
        print("Instructions: Roll 3 dice. Bet if you want to beat it. Punishments await if you lose. Every 10 rounds, spin the big die. Survive 100 rounds to win!. Respond correctly to the skeleton's question")
        answer = input("Do you wish to remove body horror?(Recommended for players <12 or players not suited to play). (Choice Yes/No): ").lower()
        if answer == "yes":
            disable_scary = True
            break
        elif answer == "no":
            disable_scary = False
            break
        else:
            clear()
    input("Press Enter to continue. Your life depends on luck and logic...")
    clear()
    while round_num <= 100 and score > 0:
        print(creep_ascii_neutral)
        if round_num % 10 == 0:
            bd()
        else:
            game()
        if score <= 0:
            break
        time.sleep(1)
        if disable_scary == False:
            punishment()
            input("Press Enter to continue...")
            anim()
        if score <= 0:
            break
        input("Press Enter to continue...")
        clear()

    clear()
    death_anim()
    while True:
        if score <= 0:
            if round_num - 1 == 100:
                print("You made it to the last round but failed. I feel bad for you. You probably didn't write the answer correctly or you ran out of score. Better luck next time.")
                print("Unlucky Ending (3/4)")
            else:
              print(f"Game Over! You survived {round_num - 1} round(s) You did not survive... You probably didn't write the answer correctly or you ran out of score. Better luck next time.")
              print("Normal Ending (1/4)")
        else:
            if devil == False:
                print(f"Congratulations! You survived 100 rounds with score {score}. It couldn't resist the meal. The odds were stacked against you anyways. There is no escape. There is no viewers. It is just It and you. You were trapped in a room but you failed to escape. Get the devil on your side.")
                print("Good-Normal (2/4)")
            else:
                clear()
                print(creep_ascii_dead)
                print("You Win. The devil blew It up. You escape.")
                print("Good Ending (4/4)")



        print("Made by Abinavram Anbuprabhu")
        print("")
        print("Another person has been captured and taken by it.")
        answer = input("Will you play again as the next person? Choice (Yes/No) ").lower()
        if answer == "yes":
            # reset all necessary variables
            print("A new game awaits")
            score = 10
            round_num = 1
            Punstate = ""
            betTimes = 3
            big_dice = 0
            anim_numb = 0
            disable_scary = False
            time.sleep(1)
            clear()
            restart_anim()
            break
        elif answer == "no":
            break
        else:
            clear()
    if answer == "no":
        break
print(creep_ascii_neutral)
input("You've quit huh? Well you made quite the challenge. Are you sure you don't want to play again? Well its too late. You're not going to change your mind. Well, I stalk you. You go to Sutton Grammar, 8 Greyhound. Your name is ########### ##########. Correct? Come back later yeah? Press Enter to continue... Bye!")