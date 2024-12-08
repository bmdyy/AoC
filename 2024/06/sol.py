#!/usr/bin/python

# Advent of Code 2024, Day 6
# William Moody (@bmdyy)
# 07.12.2024

import time

with open("input.txt","r") as f:
    inp = [list(line.strip()) for line in f.readlines()]

# Constants for describing guard's direction
D_UP, D_RIGHT, D_DOWN, D_LEFT = 0, 1, 2, 3

# Variables to keep track of size of map
rows, cols = len(inp), len(inp[0])

# Variables to keep track of guard's position and direction
g_row = 0
g_col = 0
g_dir = D_UP
g_left_map = False

# List of obstacles on the map
obs = []

# List of positions that the guard visited
visited = []

# For part two
g_in_loop = False 
g_history = [] # List of positions the guard was at, and what position he was facing

# Parse the input to determine the guard's starting position
for r in range(rows):
    for c in range(cols):
        if inp[r][c] == "#":
            obs.append((r, c))
        elif inp[r][c] == "^":
            g_row, g_col = r, c

# Remember the initial values for part 2
g_row_init = g_row
g_col_init = g_col
obs_orig = obs.copy()

# Add the guard's starting position to the visited list
visited.append((g_row, g_col))

# Moves the guard as far as possible in the current direction (until an obstacle is hit, or he leaves the map)
def step():
    global g_row, g_col, g_dir, g_left_map, obs, visited, rows, cols, g_in_loop, g_history

    if (g_row, g_col, g_dir) in g_history:
        g_in_loop = True
    else:
        g_history.append((g_row, g_col, g_dir))

        # Facing UP
        if g_dir == D_UP:
            # Calculate which obstacle is hit
            tmp_obs = [val for idx, val in enumerate(obs) if val[0] < g_row and val[1] == g_col]
            if len(tmp_obs) > 0:
                obs_hit = sorted(tmp_obs, key=lambda o: -o[0])[0]
            else:
                # Guard left the map. Create a fake obstacle for the following calculations
                obs_hit = (-1, g_col)
                g_left_map = True

            # Add all the positions inbetween that were visited
            r = g_row - 1
            while r > obs_hit[0]:
                visited.append((r, g_col))
                r -= 1

            # Update the guard's position and direction
            g_row = obs_hit[0] + 1
            g_dir = D_RIGHT

        # Facing RIGHT
        elif g_dir == D_RIGHT:
            # Calculate which obstacle is hit
            tmp_obs = [val for idx, val in enumerate(obs) if val[0] == g_row and val[1] > g_col]
            if len(tmp_obs) > 0:
                obs_hit = sorted(tmp_obs, key=lambda o: o[1])[0]
            else:
                # Guard left the map. Create a fake obstacle for the following calculations
                obs_hit = (g_row, cols)
                g_left_map = True

            # Add all the positions inbetween that were visited
            c = g_col + 1
            while c < obs_hit[1]:
                visited.append((g_row, c))
                c += 1
            
            # Update the guard's position and direction
            g_col = obs_hit[1] - 1
            g_dir = D_DOWN

        # Facing DOWN
        elif g_dir == D_DOWN:
            # Calculate which obstacle is hit
            tmp_obs = [val for idx, val in enumerate(obs) if val[0] > g_row and val[1] == g_col]
            if len(tmp_obs) > 0:
                obs_hit = sorted(tmp_obs, key=lambda o: o[0])[0]
            else:
                # Guard left the map. Create a fake obstacle for the following calculations
                obs_hit = (rows, g_col)
                g_left_map = True

            # Add all the positions inbetween that were visited
            r = g_row + 1
            while r < obs_hit[0]:
                visited.append((r, g_col))
                r += 1
            
            # Update the guard's position and direction
            g_row = obs_hit[0] - 1
            g_dir = D_LEFT

        
        # Facing LEFT
        elif g_dir == D_LEFT:
            # Calculate which obstacle is hit
            tmp_obs = [val for idx, val in enumerate(obs) if val[0] == g_row and val[1] < g_col]
            if len(tmp_obs) > 0:
                obs_hit = sorted(tmp_obs, key=lambda o: -o[1])[0]
            else:
                # Guard left the map. Create a fake obstacle for the following calculations
                obs_hit = (g_row, -1)
                g_left_map = True

            # Add all the positions inbetween that were visited
            c = g_col - 1
            while c > obs_hit[1]:
                visited.append((g_row, c))
                c -= 1
            
            # Update the guard's position and direction
            g_col = obs_hit[1] + 1
            g_dir = D_UP

t_start = time.time()
# Simulate guard's actions until he leaves the map
while not g_left_map:
    step()
t_ela = time.time() - t_start

# Remove duplicates from visited array
tmp = set()
duplicates = [pos for pos in visited if pos in tmp or tmp.add(pos)]

visited_distinct = list(dict.fromkeys(visited))
print("Part 1:", len(visited_distinct))
#print(f"(This next part should take around {round(len(visited_distinct) * t_ela, 3)} seconds)")

obs_pos_that_create_loop = []
t_start = time.time()
for r, c in visited_distinct:
    # Skip the guard's starting position
    if r == g_row_init and c == g_col_init:
        continue

    # Reset the guard's parameters
    g_row, g_col = g_row_init, g_col_init
    g_dir = D_UP
    g_left_map = False
    g_in_loop = False
    g_history = []
    
    # Add an imaginary obstacle at (r, c)
    obs.append((r, c))

    # Simulate
    while not g_left_map and not g_in_loop:
        step()

    if g_in_loop:
        obs_pos_that_create_loop.append((r, c))

    # Remove the imaginary obstacle
    obs.pop()

print("Part 2:", len(obs_pos_that_create_loop))
#print(f"(Took {round(time.time() - t_start, 3)} seconds)")