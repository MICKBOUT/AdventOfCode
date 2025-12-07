import time

input_file = "input.txt"
with open(input_file, "r") as file:
	data = [line.strip() for line in file if '^' in line or 'S' in line]

def day07_pt1(data):
	beam = set()
	beam.add(data[0].index("S"))
	res = 0
	for line in data:
		new_beam = set()
		for ell in beam:
			if line[ell] == '^':
				new_beam.add(ell - 1)
				new_beam.add(ell + 1)
				res += 1
			else:
				new_beam.add(ell)
		beam = new_beam
	return res

def day07_pt2(data):
	beam = {}
	beam[data[0].index("S")] = 1
	data = data[1:]
	for line in data:
		new_beam = {}
		for ell in beam.keys():
			if line[ell] == '^':
				if ell - 1 not in new_beam:
					new_beam[ell - 1] = beam[ell]
				else:
					new_beam[ell - 1] += beam[ell]

				if ell + 1 not in new_beam:
					new_beam[ell + 1] = beam[ell]
				else:
					new_beam[ell + 1] += beam[ell]
			else:
				if ell not in new_beam:
					new_beam[ell] = beam[ell]
				else:
					new_beam[ell] += beam[ell]
		beam = new_beam
	return sum([val for index, val in beam.items()])

s = time.time()
print(f"{day07_pt1(data)} in {round(time.time() - s, 5)}s")
s = time.time()
print(f"{day07_pt2(data)} in {round(time.time() - s, 5)}s")