class Listl():
	def __init__(self):
		self._head = Node("HEAD", None, None)                       #initialise head dummy node
		self._tail = Node("TAIL", None, None)                       #initialise tail dummy node 
		self._first = None                    						#points to where next is to be added 
		self._contents = []                                         #just a refernce of nodes added or not, not ordered

	def add_last(self, value):                                      #essentially append to the back of list
		if len(self._contents) == 0:                                #if no nodes in list
			node = 	Node(value,self._head,self._tail)               #previous pointer will be the head, next pointer will be tail
			self._first = node
			self._tail._prev = node
			self._head._after = node
			self._contents.append(node)
		else:                                                       #if already nodes in the list
			node = Node(value,self._tail._prev,self._tail)          #previous pointer will be the last node, nect pointer will be tail
			self._first = self._tail._prev      
			self._tail._prev = node
			self._first._after = node
			self._contents.append(node)
			
	def getFirst(self):
		print(self._first)
		return self._first

	def getNode(self, node):
		for val in self._contents:
			if val._element == node:
				print(val)

	

	def add_after(self, new, before):                               #add a new node in after a specific node in the list
		for val in self._contents:                                  #check that the node to add after already exists
			if val._element == before:
				nextl = val._after                                  #the node after the specific node will be pointed to by the new node
				node = Node(new, val, val._after)                   #point new node back to specific node
				val._after = node
				nextl._prev = node
				self._contents.append(node)
			else:
				continue		# print("ERROR: Item to add after is not in the list")

	def remove_node(self, node):
		for val in self._contents:
			if val._element == node:
				self._contents.remove(val)
				original_after = val._after                          #record the nodes it pointed too before being removed
				original_before = val._prev
				val = None                                           #remove it 
				original_after._prev = original_before               #point both initial nodes it pointed to to eachother
				original_before._after = original_after
			else:
				continue

	def getLength(self):
		return len(self._contents)
