import random

# ---------------------- TEAMS ----------------------
teams = {
    "India": {1: "V.Kohli", 2: "R.Sharma", 3: "S.Gill", 4: "S.Iyer", 5: "R.Jadeja",
              6: "H.Pandaya", 7: "J.Bumrah", 8: "KL.Rahul", 9: "K.Yadav", 10: "M.Shami", 11: "M.Siraj"},
    "Pakistan": {1: "B.Azam", 2: "F.Zaman", 3: "S.Afridi", 4: "M.Rizwan", 5: "A.Shafique",
                 6: "H.Rauf", 7: "S.Khan", 8: "Imam-ul-Haq", 9: "I.Khan", 10: "H.Ali", 11: "Z.Khan"},
    "England": {1: "B.Duckett", 2: "J.Root", 3: "O.Pope", 4: "Z.Crawley", 5: "B.Stokes",
                6: "R.Ahmed", 7: "B.Foakes", 8: "A.Rashid", 9: "J.Anderson", 10: "M.Wood", 11: "A.Cook"}
}


# ---------------------- INPUT HELPERS ----------------------
def get_valid_input(prompt, valid_range):
    """Ask until valid integer in range is entered"""
    while True:
        try:
            val = int(input(prompt))
            if val in valid_range:
                return val
            print(f"❌ Invalid choice! Enter a number between {min(valid_range)} and {max(valid_range)}.")
        except ValueError:
            print("❌ Please enter a valid number.")


# ---------------------- GAME FUNCTIONS ----------------------
def choose_team():
    """Let player choose team and players safely"""
    print("Choose your team:")
    team_names = list(teams.keys())
    for i, t in enumerate(team_names, 1):
        print(f"{i}. {t}")

    choice = get_valid_input("Enter your choice (1-3): ", range(1, 4))
    player_team = team_names[choice - 1]
    opponent = random.choice([t for t in team_names if t != player_team])

    print(f"\n✅ Your team is {player_team}: \n{teams[player_team]}")
    print(f"⚔️ Opponent is {opponent}: \n{teams[opponent]}\n")

    wickets = get_valid_input("Enter number of wickets to play with: ", range(1, 12))
    player_list = []
    print("\nChoose your players by ID:")

    while len(player_list) < wickets:
        pid = get_valid_input("Enter player ID: ", teams[player_team].keys())
        if teams[player_team][pid] not in player_list:
            player_list.append(teams[player_team][pid])
        else:
            print("❌ Player already selected! Choose another.")

    print("🎯 Your Playing XI:", player_list)
    return player_team, opponent, wickets


def play_innings(overs, wickets, batting_first=True, target=None):
    """Simulates one innings"""
    balls, score, outs = overs * 6, 0, 0

    for ball in range(1, balls + 1):
        if outs >= wickets: break

        user = get_valid_input("Enter your choice (1-6): ", range(1, 7))
        comp = random.randint(1, 6)

        if batting_first:  # user batting
            print("Computer bowls:", comp)
            if user == comp:
                outs += 1; print(f"🚨 OUT! Wickets left: {wickets - outs}")
            else:
                score += user
        else:  # user bowling
            print("Computer hits:", comp)
            if user == comp:
                outs += 1; print(f"🚨 OUT! Computer wickets left: {wickets - outs}")
            else:
                score += comp

        print(f"Ball {ball}: Score = {score}/{outs}\n")

        # Over update
        if ball % 6 == 0:
            print(f"--- End of Over {ball//6} --- Score: {score}/{outs}\n")

        # Stop if target reached
        if target and score >= target: break

    return score, outs


def play_match():
    overs = get_valid_input("Enter number of overs: ", range(1, 51))
    player_team, opponent, wickets = choose_team()

    print("\n---------------- TOSS ----------------")
    toss = random.choice(["Head", "Tail"])
    call = input("Call Head or Tail: ").capitalize()
    print(f"Toss result: {toss}")

    if toss == call:
        print("🎉 You won the toss!")
        user_choice = input("Choose Batting or Bowling (Bat/Bowl): ").lower()
    else:
        user_choice = random.choice(["bat", "bowl"])
        print(f"🤖 Computer won the toss and chose to {user_choice} first.")

    # First innings
    if user_choice.startswith("b"):  # user bats first
        print("\n--------- 1st Innings (You Bat) ---------")
        pscore, pwkts = play_innings(overs, wickets, True)
        target = pscore + 1
        print(f"\nYour innings ends at {pscore}/{pwkts}. Target: {target}")

        print("\n--------- 2nd Innings (You Bowl) ---------")
        cscore, cwkts = play_innings(overs, wickets, False, target)
    else:  # computer bats first
        print("\n--------- 1st Innings (You Bowl) ---------")
        cscore, cwkts = play_innings(overs, wickets, False)
        target = cscore + 1
        print(f"\nComputer scored {cscore}/{cwkts}. Target: {target}")

        print("\n--------- 2nd Innings (You Bat) ---------")
        pscore, pwkts = play_innings(overs, wickets, True, target)

    # Match result
    print("\n---------------- RESULT ----------------")
    if user_choice.startswith("b"):  # user batted first
        if cscore >= target:
            print(f"🏆 {opponent} won by {wickets - cwkts} wickets!")
        else:
            print(f"🏆 You won by {target - 1 - cscore} runs!")
    else:
        if pscore >= target:
            print(f"🏆 You won by {wickets - pwkts} wickets!")
        else:
            print(f"🏆 {opponent} won by {target - 1 - pscore} runs!")


# ---------------------- MAIN LOOP ----------------------
print("\n================ HAND CRICKET ================")
while True:
    play_match()
    if input("\nPlay again? (Y/N): ").upper() == "N":
        print("Thanks for playing! 👋")
        break
