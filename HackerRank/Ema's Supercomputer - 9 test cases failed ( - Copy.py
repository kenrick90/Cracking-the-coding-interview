# Ema's Supercomputer
# https://www.hackerrank.com/challenges/two-pluses/problem

#return row index, column index and area of largest
def getLargestArea(grid,n,m):

	maxarea=0

	#find the largest plus in maxi maxj and maxarea
	for i in range(n):
		for j in range(m):
			if grid[i][j] == 'G':
				area = 1
				if area > maxarea:
					maxarea = area
					maxi = i
					maxj = j
				iPossible = min(i,n-i-1)
				jPossible = min(j,m-j-1)
				possible = min(iPossible,jPossible)
				for k in range(1,possible+1):
					if grid[i+k][j] == 'G' and grid[i-k][j] =='G' and grid[i][j+k] == 'G' and grid[i][j-k] == 'G':
						area = 1+(k*4)
						if area > maxarea:
							maxi = i
							maxj = j
							maxarea = area
					else:
						break
	return maxi, maxj, maxarea	

def twoPluses(grid, n, m):

	maxi,maxj,maxarea = getLargestArea(grid,n,m)
	#Consider the largest plus's square as 'B'					
	k = int(maxarea/4 -0.25)
	grid[maxi][maxj] = 'B'
	for i in range(1,k+1):
		grid[maxi+i][maxj] = 'B'
		grid[maxi-i][maxj] = 'B'
		grid[maxi][maxj+i] = 'B'
		grid[maxi][maxj-i] = 'B'

	secondMaxi,secondMaxj,Secondmaxarea = getLargestArea(grid,n,m)

	return Secondmaxarea*maxarea



if __name__ == "__main__":
	n, m = list(map(int,input().rstrip().split()))
	grid = []
	for _ in range(n):
		row = input()
		newrow = []
		for character in row:
			newrow.append(character)
		grid.append(newrow)

	print(twoPluses(grid, n, m))