#!/usr/bin/python

# Advent of Code 2024, Day 5
# William Moody (@bmdyy)
# 06.12.2024

import time

with open("input.txt","r") as f:
    inp = [list(line.strip()) for line in f.readlines()]

rows, cols = len(inp), len(inp[0])
guard_r, guard_c = 0, 0
guard_dir = "UP"
guard_left_board = False
obstacles = []

for r in range(rows):
    for c in range(cols):
        if inp[r][c] == "^":
            guard_r, guard_c = r, c
        elif inp[r][c] == "#":
            obstacles.append((r, c))

init_guard_r, init_guard_c = guard_r, guard_c

visited = [(guard_r, guard_c)]
visited_with_dir = [(guard_r, guard_c, guard_dir)]

def do_step(obstacles, set_visited=True):
    global rows, cols, guard_r, guard_c, guard_dir, guard_left_board, visited

    if guard_dir == "UP":
        if guard_r > 0:
            if (guard_r-1, guard_c) in obstacles:
                guard_dir = "RIGHT"
            else:
                guard_r -= 1
        else:
            guard_left_board = True
    elif guard_dir == "DOWN":
        if guard_r < rows-1:
            if (guard_r+1, guard_c) in obstacles:
                guard_dir = "LEFT"
            else:
                guard_r += 1
        else:
            guard_left_board = True
    elif guard_dir == "LEFT":
        if guard_c > 0:
            if (guard_r, guard_c-1) in obstacles:
                guard_dir = "UP"
            else:
                guard_c -= 1
        else:
            guard_left_board = True
    elif guard_dir == "RIGHT":
        if guard_c < cols-1:
            if (guard_r, guard_c+1) in obstacles:
                guard_dir = "DOWN"
            else:
                guard_c += 1
        else:
            guard_left_board = True

    if set_visited:
        if not (guard_r, guard_c) in visited:
            visited.append((guard_r, guard_c))

        visited_with_dir.append((guard_r, guard_c, guard_dir))

while not guard_left_board:
    do_step(obstacles=obstacles)

print("Part 1:",len(visited))

solutions = []
for (r,c,d) in visited_with_dir:
    obs_r, obs_c = -1, -1
    if d == "UP" and r > 0:
        obs_r, obs_c = r-1, c
    elif d == "LEFT" and c > 0:
        obs_r, obs_c = r, c-1
    elif d == "DOWN" and r < rows-1:
        obs_r, obs_c = r+1, c
    elif d == "RIGHT" and c < cols-1:
        obs_r, obs_c = r, c+1

    if ((obs_r, obs_c) in solutions) or (obs_r < 0 and obs_c < 0) or (obs_r == init_guard_r and obs_c == init_guard_c):
        continue

    tmp_obstacles = obstacles.copy()
    tmp_obstacles.append((obs_r, obs_c))
    #print(tmp_obstacles)

    guard_r, guard_c = init_guard_r, init_guard_c
    guard_dir = "UP"
    guard_left_board = False
    is_loop = False
    t_start = time.time()
    while (not is_loop) and (not guard_left_board):
        do_step(obstacles=tmp_obstacles, set_visited=False)

        is_loop = (time.time() - t_start > 1)

    if is_loop:
        sol = (obs_r, obs_c)
        print(sol)
        solutions.append(sol)

print("Part 2:",len(solutions))