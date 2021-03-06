class Node():
	def __init__(self, element, prev=None, after=None):     #create a node
		self._element = element 
		self._prev = prev                                     #refernce to an object
		self._after = after                                   #refernce to an object

	def __str__(self):                                      #print the node element with its two pointers
		return "{}<--[{}]-->{}".format(self._prev._element, self._element, self._after._element)

	def getElement(self):
		return self._element

	def getNext(self):
		return self._after

	def getPrevious(self):
		return self._prev
