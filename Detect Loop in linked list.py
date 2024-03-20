#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        s = set()
        temp = head
        while (temp):
 
            # If we already have
            # this node in hashmap it
            # means there is a cycle
            # (Because we are encountering
            # the node second time).
            if (temp in s):
                return True
 
            # If we are seeing the node for
            # the first time, insert it in hash
            s.add(temp)
 
            temp = temp.next
 
        return False
