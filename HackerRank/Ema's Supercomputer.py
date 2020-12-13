# Ema's Supercomputer
# https://www.hackerrank.com/challenges/two-pluses/problem

#return row index, column index and area of largest

def twoPluses(grid, n, m):
	area =0
	for i in range(1,n+1):
		for j in range(1,m+1):
			r = 0
			while grid[i+r][j] == 'G' and grid[i-r][j] =='G' and grid[i][j+r] == 'G' and grid[i][j-r] == 'G':
				grid[i+r][j] = grid[i-r][j] = grid[i][j+r] = grid[i][j-r] = 'g'
				for I in range(1,n+1):
					for J in range(1,m+1):
						R=0
						while grid[I+R][J] == 'G' and grid[I-R][J] =='G' and grid[I][J+R] == 'G' and grid[I][J-R] == 'G':
							area = max(area, (1+4*r) * (1+4*R))
							R+=1
				r += 1
			r=0
			while grid[i+r][j] == 'g' and grid[i-r][j] =='g' and grid[i][j+r] == 'g' and grid[i][j-r] == 'g':
				grid[i+r][j] = grid[i-r][j] = grid[i][j+r] = grid[i][j-r] = 'G'
				r+=1
	return area



if __name__ == "__main__":
	n, m = list(map(int,input().rstrip().split()))
	grid = []

	grid.append(['0' for _ in range(m+2)])
	for _ in range(n):
		row = '0' + input() + '0'
		newrow = []
		for character in row:
			newrow.append(character)
		grid.append(newrow)
	grid.append(['0' for _ in range(m+2)])
	print(twoPluses(grid,n,m))