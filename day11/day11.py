input_file = "input2.txt"
with open(input_file, "r") as file:
	dico = {}
	for line in file:
		line = line.strip()
		key, value = line.split(":")
		dico[key] = set(value[1:].split(" "))

# this way work bc i know the grap is one way whit no comming back
# and i know that srv is before fft and fft is before dac

def day11_pt2(dico, path):
	seen = {"out"}
	path = path[::-1]
	res = 1
	for i in range(len(path) - 1):
		new_seen = set()
		res *= explore(path[i + 1], path[i], dico, seen, new_seen)
		seen = seen.union(new_seen)
	return res

def explore(node, goal, dico, seen, new_seen):
	res = 0
	for neighbor in dico[node]:
		if neighbor == goal:
			res += 1
		elif neighbor not in seen:
			new_seen.add(node)
			res += explore(neighbor, goal, dico, seen, new_seen)
	return res

print(day11_pt2(dico, ["svr", "fft", "dac", "out"]))