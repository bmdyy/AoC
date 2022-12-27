#!/usr/bin/python3

# William Moody
# 27.12.2022

# Part One
data = open("input.txt", "r").read().split("\n")
totalScore = 0
for i in range(len(data)):
    opp, you = data[i].split(" ")
    if opp == "A": # Rock
        if you == "X": # Rock (Tie)
            score = 1 + 3
        elif you == "Y": # Paper (Win)
            score = 2 + 6
        else: # Scissors (Lose)
            score = 3 + 0
    elif opp == "B": # Paper
        if you == "X": # Rock (Lose)
            score = 1 + 0
        elif you == "Y": # Paper (Tie)
            score = 2 + 3
        else: # Scissors (Win)
            score = 3 + 6
    else: # Scissors
        if you == "X": # Rock (Win)
            score = 1 + 6
        elif you == "Y": # Paper (Lose)
            score = 2 + 0
        else: # Scissors (Tie)
            score = 3 + 3
    totalScore += score
print(totalScore)

# Part Two
data = open("input.txt", "r").read().split("\n")
totalScore = 0
for i in range(len(data)):
    opp, you = data[i].split(" ")
    if opp == "A": # Rock
        if you == "X": # Lose (Scissors)
            score = 0 + 3
        elif you == "Y": # Tie (Rock)
            score = 3 + 1
        else: # Win (Paper)
            score = 6 + 2
    elif opp == "B": # Paper
        if you == "X": # Lose (Rock)
            score = 0 + 1
        elif you == "Y": # Tie (Paper)
            score = 3 + 2
        else: # Win (Scissors)
            score = 6 + 3
    else: # Scissors
        if you == "X": # Lose (Paper)
            score = 0 + 2
        elif you == "Y": # Tie (Scissors)
            score = 3 + 3
        else: # Win (Rock)
            score = 6 + 1
    totalScore += score
print(totalScore)