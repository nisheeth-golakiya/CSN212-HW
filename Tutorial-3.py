'''Implementation of Interval Tree'''
class Interval(object):
	'''Implementation of Interval data-type'''
	def __init__(self, low, high):
		super(Interval, self).__init__()
		self.low = low
		self.high = high
		
class Node(object):
	'''Implementation of Node data-type'''
	def __init__(self, interval):
		super(Node, self).__init__()
		self.i = interval
		self.max = interval.high
		self.l_child = None
		self.r_child = None

def insert(node, interval):
	'''Similar to BST insert keyed on low endpoint of intervals'''
	if node is None:
		return Node(interval)

	if interval.low < node.i.low :
		node.l_child = insert(node.l_child, interval)
	else :
		node.r_child = insert(node.r_child, interval)

	if node.max < interval.high :
		node.max = interval.high

	return node

def search(node, interval):
	if node is None :
		raise KeyError('Error, interval not in the tree')

	if checkOverlap(node.i, interval):
		print "Overlap found at [",node.i.low, node.i.high,"]"
		return

	if node.l_child is not None:
		if node.l_child.max >= interval.low:
			return search(node.l_child, interval)

	return search(node.r_child, interval)

def inorder(node):
	if node is None:
		return

	inorder(node.l_child)
	print "[",node.i.low, node.i.high,"]", "max = ", node.max
	inorder(node.r_child)

def checkOverlap(i1, i2):
	if (i1.low <= i2.high) & (i2.low <= i1.high):
		return True
	return False

def main():
	intervals = [Interval(0,3), Interval(5,8), Interval(26,26), Interval(25,30),\
	 Interval(15,23), Interval(19,20), Interval(17,19), Interval(8,9)]
	root = None
	for i in intervals:
		root = insert(root, i)
	inorder(root)
	search(root, Interval(6,10))

if __name__ == '__main__':
	main()
		
		