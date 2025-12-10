import time

input_file = "input.txt"
with open(input_file, "r") as file:
	arrey = [line.strip().split(' ') for line in file]
	button = [sorted([[int(y) for y in x[1:-1].split(',')] for x in line[1:-1]], key=len, reverse=True) for line in arrey]
	need = [[int(y) for y in line[-1][1:-1].split(',')] for line in arrey]

from math import ceil

def day10_pt2_line(button_lst, need, i=0, push=0, current=None, best=None):
    if current is None:
        current = [0] * len(need)
    if best is None:
        best = [float("inf")]

    if current == need:
        best[0] = min(best[0], push)
        return best[0]

    if any(c > n for c, n in zip(current, need)) or push >= best[0]:
        return best[0]

    if i == len(button_lst):
        return best[0]

    bt = button_lst[i]

    R = sum(max(0, need[j] - current[j]) for j in range(len(need)))
    M = max((len(S) for S in button_lst if S), default=0)
    lb = ceil(R / M) if M > 0 else 0
    if push + lb >= best[0]:
        return best[0]

    kmax = min(need[j] - current[j] for j in bt)
    if kmax < 0:
        return best[0]

    for k in range(kmax, -1, -1):
        if k:
            for j in bt:
                current[j] += k
        day10_pt2_line(button_lst, need, i+1, push+k, current, best)
        if k:
            for j in bt:
                current[j] -= k

    return best[0]

import pulp

def solve_machine(buttons, need):
    # Crée un problème d’optimisation
    prob = pulp.LpProblem("Machine", pulp.LpMinimize)

    # Variables : nombre d’appuis par bouton
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(len(buttons))]

    # Objectif : minimiser le total d’appuis
    prob += pulp.lpSum(x)

    # Contraintes : chaque compteur atteint sa cible
    for j in range(len(need)):
        prob += pulp.lpSum(x[i] for i, S in enumerate(buttons) if j in S) == need[j]

    # Résolution
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    if pulp.LpStatus[prob.status] != "Optimal":
        return None
    return sum(v.value() for v in x)

def day10_pt2(buttons, needs):
    total = 0
    for i, (btns, need) in enumerate(zip(buttons, needs)):
        res = solve_machine(btns, need)
        print(f"{i+1}: {res}")
        total += res
    return total



print(day10_pt2(button, need))

# for line in arrey: print(line)

# def c_list_add(c_list, max_button):
# 	i = 0
# 	while i < len(c_list):
# 		if c_list[i] < max_button:
# 			c_list[i] += 1
# 			for j in range(i):
# 				c_list[j] = 0
# 			return c_list
# 		else:
# 			i += 1
# 	c_list.append(0)
# 	return c_list	

# def is_valide(c_list, display, button):
# 	goal = [-1] * len(display)
# 	for bt_lst in c_list:
# 		for bt in button[bt_lst]:

# 			goal[bt] *= -1
# 	for i in range(len(goal)):
# 		if goal[i] == -1 and display[i] == '#':
# 			return (False)
# 		elif goal[i] == 1 and display[i] == '.':
# 			return (False)
# 	return True

# def day10(arrey):
# 	display = [line[0] for line in arrey]
# 	button = [line[1][:-1] for line in arrey]
# 	res = 0
# 	for i in range(len(arrey)):
# 		c_list = [0] * 1
# 		while not is_valide(c_list, display[i], button[i]):
# 			c_list = c_list_add(c_list, len(button[i]) - 1)
# 		print(f"{i}/{len(arrey)}, c = {len(c_list)}")
# 		res += len(c_list)
# 	return res
	
# print(day10(arrey))