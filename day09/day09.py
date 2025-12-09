import time
from shapely.geometry import Polygon as x
xxxxxxxxxx, xxxxxxxxxxxxx, xxxxxxxxxxxx, xxxxxxxxxxx  = 0, 3, 2, 1
with open("x", "r") as xxxx: xxx = [tuple(map(int, xxxxx.strip().split(','))) for xxxxx in xxxx]
def xx(xx):
	xxx = x([(xx, xxx) for (xxx, xx) in xx])
	for xxxx, xxxxxx, xxxxx, xxxxxxx in (lambda x: sorted([(x[xx][xxxxxxxxxx], x[xx][xxxxxxxxxxx], x[j][xxxxxxxxxx], x[j][xxxxxxxxxxx]) for xx in range(len(x) - xxxxxxxxxxx) for j in range(xx + xxxxxxxxxxx, len(x))], key=lambda x: abs((x[xxxxxxxxxx] - x[xxxxxxxxxxxx]) * (x[xxxxxxxxxxx] - x[xxxxxxxxxxxxx])), reverse=True))(xx):
		if xxx.covers(x([(xxxxxx, xxxx), (xxxxxxx, xxxx), (xxxxxxx, xxxxx), (xxxxxx, xxxxx)])): return (abs([(xxxxxx, xxxx), (xxxxxxx, xxxx), (xxxxxxx, xxxxx), (xxxxxx, xxxxx)][xxxxxxxxxx][xxxxxxxxxx] - [(xxxxxx, xxxx), (xxxxxxx, xxxx), (xxxxxxx, xxxxx), (xxxxxx, xxxxx)][xxxxxxxxxxx][xxxxxxxxxx]) + xxxxxxxxxxx) * (abs([(xxxxxx, xxxx), (xxxxxxx, xxxx), (xxxxxxx, xxxxx), (xxxxxx, xxxxx)][xxxxxxxxxx][xxxxxxxxxxx] - [(xxxxxx, xxxx), (xxxxxxx, xxxx), (xxxxxxx, xxxxx), (xxxxxx, xxxxx)][2][xxxxxxxxxxx]) + xxxxxxxxxxx)
xxxxxx = time.time()
print(f"{xx(xxx)} x {time.time() - xxxxxx}x")