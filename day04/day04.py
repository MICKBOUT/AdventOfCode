input_file = "input.txt"
with open(input_file, "r") as file:
	arrey = [[x for x in line.strip()] for line in file]

def day04_v1(matrix):
	res = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == '@':
				arround = 0
				for k in range(max(i - 1, 0), min(i + 2, len(matrix))):
					for l in range(max(j - 1, 0), min(j + 2, len(matrix[j]))):
						if matrix[k][l] == '@':
							arround += 1
				if (arround <= 4):
					res += 1
	return (res)


def day04_v2(matrix):
	res = 0
	change = True
	while (change):
		change = False
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				if matrix[i][j] == '@':
					arround = 0
					for k in range(max(i - 1, 0), min(i + 2, len(matrix))):
						for l in range(max(j - 1, 0), min(j + 2, len(matrix[j]))):
							if matrix[k][l] == '@':
								arround += 1
					if (arround <= 4):
						res += 1
						matrix[i][j] = '.'
						change = True
	return (res)
print(day04_v2(arrey))