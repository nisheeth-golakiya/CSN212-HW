import numpy as np
import time

# Function to know if we have a counter-clockwise turn
def CCW(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return True
	return False

# Gift wrapping algorithm
def GiftWrapping(S):
	n = len(S)
	P = [None] * n
	l = np.where(S[:,0] == np.min(S[:,0]))
	pointOnHull = S[l[0][0]]
	i = 0
	while True:
		P[i] = pointOnHull
		endpoint = S[0]
		for j in range(1,n):
			if (endpoint[0] == pointOnHull[0] and endpoint[1] == pointOnHull[1]) or not CCW(S[j],P[i],endpoint):
				endpoint = S[j]
		i = i + 1
		pointOnHull = endpoint
		if endpoint[0] == P[0][0] and endpoint[1] == P[0][1]:
			break
	for i in range(n):
		if P[-1] == None:
			del P[-1]
	return np.array(P)

def main():
	
	P = np.array([(np.random.randint(0,300),np.random.randint(0,300)) for i in range(50)])
	start = time.clock()
	L = GiftWrapping(P)
	end = time.clock()
	
	for l in L:
		print(l)
		
	print "Time consumed: ", end - start

if __name__ == '__main__':
    main()
