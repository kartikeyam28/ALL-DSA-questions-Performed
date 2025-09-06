import sys

knightpos = [int(x) for x in sys.argv[1].split(',')]
targetpos = [int(x) for x in sys.argv[2].split(',')]
n = int(sys.argv[3])

def minStepToReachTarget(knightpos, targetpos, n):
	moves = [
		(-2, -1), (-1, -2), (1, -2), (2, -1),
		(-2, 1), (-1, 2), (1, 2), (2, 1)]

	visited = [[False for _ in range(n+1)] for  _ in range(n+1)]
	queue = [(knightpos[0], knightpos[1], 0)]
	visited[knightpos[0]][knightpos[1]] = True
	while queue:
		x, y, steps = queue[0]
		queue = queue[1:]

		if x == targetpos[0] and y == targetpos[1]:
			return steps

		for dx, dy in moves:
			nx, ny = x + dx, y + dy
			if 1 <= nx <= n and 1 <= ny <= n and not visited[nx][ny]:
				visited[nx][ny] = True
				queue.append((nx, ny, steps + 1))

	return -1
	
print(minStepToReachTarget(knightpos, targetpos, n))