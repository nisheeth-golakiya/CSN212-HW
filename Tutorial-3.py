'''Implementation of Interval Tree by augmenting BST'''

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
	#If tree is empty, make a new node
	if node is None:
		return Node(interval)
	
	#key less than current value, insert in left subtree
	#else insert in right subtree
	if interval.low < node.i.low :
		node.l_child = insert(node.l_child, interval)
	else :
		node.r_child = insert(node.r_child, interval)
		
	#update max
	if node.max < interval.high :
		node.max = interval.high

	return node

def search(node, interval):
	#Base case : tree is empty
	if node is None :
		raise KeyError('Error, interval not in the tree')
		
	#Base case 2 : check for overlap
	if checkOverlap(node.i, interval):
		print "Overlap found at [",node.i.low, node.i.high,"]"
		return
	
	#If non-empty left child has larger max than low endpoint of the interval
	#search in left subtree
	if node.l_child is not None:
		if node.l_child.max >= interval.low:
			return search(node.l_child, interval)

	#else search in right subtree
	return search(node.r_child, interval)

def delete(node, interval):
	#Base case : tree is empty
	if node is None :
		return node

	#Search the node to be deleted
	if interval.low < node.i.low :
		node.l_child = delete(node.l_child, interval)

	elif interval.low > node.i.low :
		node.r_child = delete(node.r_child, interval)
		
	#Got the node, now delete
	else :
		#If node has only one or zero child
		if node.l_child is None :
			temp = node.r_child
			node = None
			return temp

		elif node.r_child is None :
			temp = node.l_child
			node = None
			return temp

		#If node has two children
		#find its successor in its inorder traversal and replace it
		temp = find_successor(node.r_child)
		node.i = temp.i
		node.r_child = delete(node.r_child, temp.i)
	#Update max
	node = maxUpdate(node)
	return node

#Utility functions
def find_successor(node):
	current = node
	while current.l_child is not None:
		current = current.l_child
	return current

def maxUpdate(node):
	if node is None:
		return
	maxUpdate(node.l_child)
	maxUpdate(node.r_child)
	if node.r_child is not None :
		if node.l_child is not None :
			node.max = max(node.l_child.max, node.r_child.max, node.i.high)
		else :
			node.max = max(node.r_child.max, node.i.high)
	else :
		if node.l_child is not None :
			node.max = max(node.l_child.max, node.i.high)
		else :
			node.max = node.i.high
	return node

def inorder(node):
	if node is None:
		return

	inorder(node.l_child)
	print "[",node.i.low, node.i.high,"]", "max = ", node.max
	inorder(node.r_child)

def checkOverlap(i1, i2):
	#check if the given two intervals overlap
	if (i1.low <= i2.high) & (i2.low <= i1.high):
		return True
	return False

def main():
	intervals = [Interval(15,23), Interval(5,8), Interval(0,3), Interval(8,9), Interval(19,20),\
	 Interval(17,19), Interval(25,30)]
	root = None
	for i in intervals:
		root = insert(root, i)
	inorder(root)
	print ("Search interval (6,10)")
	search(root, Interval(6,10))
	print ("After deleting interval (25,30)")
	root = delete(root, Interval(25,30))
	inorder(root)
	print ("After deleting interval (15,23)")
	root = delete(root, Interval(15,23))
	inorder(root)
	
if __name__ == '__main__':
	main()	
