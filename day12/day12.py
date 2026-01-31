
input_file = "input.txt"
with open(input_file, "r") as file:
	arrey = [line.strip() for line in file]
	arrey = [((tuple(map(int, line[:line.index(":")].split('x')))), tuple(map(int, line[line.index(" ") + 1:].split(" ")))) for line in arrey]


tuile0 =	[[(0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2)],
			[(1, 2), (2, 2), (0, 1), (1, 1), (0, 0), (1, 0), (2, 0)],
			[(2, 1), (2, 0), (1, 2), (1, 1), (0, 2), (0, 1), (0, 0)],
			[(1, 0), (0, 0), (2, 1), (1, 1), (2, 2), (1, 2), (0, 2)]]
tuile1 =	[[(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)],
			[(0, 2), (2, 2), (0, 1), (2, 1), (0, 0), (1, 0), (2, 0)],
			[(2, 2), (2, 0), (1, 2), (1, 0), (0, 2), (0, 1), (0, 0)],
			[(2, 0), (0, 0), (2, 1), (0, 1), (2, 2), (1, 2), (0, 2)]]
tuile2 =	[[(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)],
			[(0, 2), (1, 2), (1, 1), (2, 1), (2, 0)],
			[(2, 2), (2, 1), (1, 1), (1, 0), (0, 0)],
			[(2, 0), (1, 0), (1, 1), (0, 1), (0, 2)]]
tuile3 =	[[(0, 2), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
			[(2, 2), (1, 1), (2, 1), (0, 0), (1, 0), (2, 0)],
			[(2, 0), (1, 1), (1, 0), (0, 2), (0, 1), (0, 0)],
			[(0, 0), (1, 1), (0, 1), (2, 2), (1, 2), (0, 2)]]
tuile4 =	[[(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2)],
			[(0, 2), (1, 2), (2, 2), (1, 1), (2, 1), (1, 0), (2, 0)],
			[(2, 2), (2, 1), (2, 0), (1, 1), (1, 0), (0, 1), (0, 0)],
			[(2, 0), (1, 0), (0, 0), (1, 1), (0, 1), (1, 2), (0, 2)]]
tuile5 =	[[(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)],
			[(0, 2), (1, 2), (2, 2), (1, 1), (0, 0), (1, 0), (2, 0)],
			[(2, 2), (2, 1), (2, 0), (1, 1), (0, 2), (0, 1), (0, 0)],
			[(2, 0), (1, 0), (0, 0), (1, 1), (2, 2), (1, 2), (0, 2)]]

tiles = [tuile0,tuile1,tuile2,tuile3,tuile4,tuile5]

def tuile_surface(tile_orientations):
    # toutes les orientations ont la même surface (# de cases)
    return len(tile_orientations[0])

valid_count = 0

for (dims, counts) in arrey:
    width, height = dims
    grid_area = width * height

    # surface totale des tuiles demandées
    total_tiles_area = sum(counts[i] * tuile_surface(tiles[i]) for i in range(len(tiles)))

    if total_tiles_area <= grid_area:
        valid_count += 1

print("Nombre de grilles valides (surface possible) :", valid_count)