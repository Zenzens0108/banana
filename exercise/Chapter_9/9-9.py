"""
G R
O K
"""
points = []
with open('coord.txt', 'r') as f:
    n = int(f.readline().strip())
    for _ in range(n):
        x, y = map(int, f.readline().strip().split())
        points.append((x, y))
points.sort()

for x, y in points:
    print(f"{x} {y}")