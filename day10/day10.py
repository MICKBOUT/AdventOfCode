
input_file = "input.txt"
with open(input_file, "r") as file:
	arrey = [line.strip() for line in file]
	arrey = [(line[:line.index(']') + 1][1:-1], line[line.index(']') + 2:].split(' ')) for line in arrey]
	arrey = [(line[0], [tuple(map(int, c[1:-1].split(','))) for c in line[1]]) for line in arrey]


def c_list_add(c_list, max_button):
	i = 0
	while i < len(c_list):
		if c_list[i] < max_button:
			c_list[i] += 1
			for j in range(i):
				c_list[j] = 0
			return c_list
		else:
			i += 1
	c_list.append(0)
	return c_list	

def is_valide(c_list, display, button):
	goal = [-1] * len(display)
	for bt_lst in c_list:
		for bt in button[bt_lst]:

			goal[bt] *= -1
	for i in range(len(goal)):
		if goal[i] == -1 and display[i] == '#':
			return (False)
		elif goal[i] == 1 and display[i] == '.':
			return (False)
	return True

def day10(arrey):
	display = [line[0] for line in arrey]
	button = [line[1][:-1] for line in arrey]
	res = 0
	for i in range(len(arrey)):
		c_list = [0] * 1
		while not is_valide(c_list, display[i], button[i]):
			c_list = c_list_add(c_list, len(button[i]) - 1)
		print(f"{i}/{len(arrey)}, c = {len(c_list)}")
		res += len(c_list)
	return res
	
print(day10(arrey))