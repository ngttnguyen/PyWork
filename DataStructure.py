#!/usr/bin/env python
# coding: utf-8

# # Linked list
# 

# In[13]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.start = None
    # Insert function
    def insert(self, value):
        if self.start == None:
            self.start = Node(value)
        else:
            current = self.start
            while current.next is not None:
                current = current.next
                
            current.next = Node(value)
    
    def delete(self, value):
        
    # Print LinkedList
    def printLinkedList(self):
        current = self.start
        if(current == None):
            print("The linked list is empty.")
        else:
            while current is not None:
                print(current.value,end = " ")
                current = current.next

ll = LinkedList()
ll.printLinkedList()
ll.insert(2)
ll.insert("acc")
ll.printLinkedList()        


# # LIST

# In[25]:


firstList = [1, 'abc',[30,'hanza']]
print(firstList[2])

fruits = ['apple', 'orange']
print(fruits)
fruits.append(67)
#fruits.extend('mango')
fruits.insert(0,'banana')
print(fruits)


# # Queue

# In[29]:


class Queue:
    def __init__(self):
        self.queue = list()
        self.first = -1
        self.last = -1
        
    def enqueue(self, value):
        if self.first == -1:
            self.first += 1
        self.last += 1
        self.queue.insert(self.last, value)
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.queue)
print(queue.first)
print(queue.last)


# # STACK

# In[35]:


class Stack:
    def __init__(self):
        self.stack = list()
        
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        if(len(self.stack) < 1):
            print("The stack is empty")
        else:
            item = self.stack.pop()
            return(item)
    
    def printStack(self):
        if(len(self.stack) < 1):
            print("The stack is empty")
        else:
            print(self.stack)
        
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.printStack()
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

stack.printStack()


# # BSTREE

# In[71]:


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def insert(root, node):
    if root is None:
        root = node
        return root
    
    if node.value < root.value:
        root.left = insert(root.left, node)
        
    if node.value > root.value:
        root.right = insert(root.right, node)
       
    return root

def preorder(root):
    if root is None:
        return
    else:
    
        print(root.value, end = " ")

        preorder(root.left)
        preorder(root.right)
    return

def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left) 
        print(root.value, end = " ")
        inorder(root.right)
    return

def postorder(root):
    if root is None:
        return
    else:
        postorder(root.left) 
        postorder(root.right)
        print(root.value, end = " ")
    return

def getMinValueNode(root):
    if root is not None:
        while root.left is not None:
            root = root.left
        return root

def findNode(root, value):
    tem = None
    if root is None:
        return None
    else:
        if (root.value < value):
            tem = findNode(root.right, value)
        elif root.value == value:
            tem = root
        else:
            tem = findNode(root.left, value)
        return tem
                    

def deleteNode(root, value):
    
    if value < root.value:
        root.left = deleteNode(root.left, value)
    elif value > root.value:
        root.right = deleteNode(root.right, value)
    else:
        if root.left is None:
            return(root.right)
            
        elif root.right is None:
            return root.left
        
        else:
            temp = getMinValueNode(root.right)
            root.value = temp.value
            root.right = deleteNode(root.right, temp.value)     
    
    return root
        
        
   
        
    
tree = None
tree = Node(7)
insert(tree, Node(10))
insert(tree, Node(90))
insert(tree, Node(8))
insert(tree, Node(9))
insert(tree, Node(4))
preorder(tree)
print('\n---------')

temp = deleteNode(tree, 7)
preorder(temp)
print('\n')
preorder(tree)
print('\n---------')

print(temp)
print(tree)



# # Algorithm

# In[84]:


# Insertion
def insertionSort(mylist):
    for i in range(1, len(mylist)):
        value = mylist[i]
        j = i
        while (j > 0 and mylist[j - 1] > value ):
            mylist[j] = mylist[j -1]
            j -= 1
        
        mylist[j] = value
        
def selectionSort(mylist):
    for i in range(0, len(mylist) -1):
        minValueIndex = i
        for j in range(i+1, len(mylist)):
            if(mylist[minValueIndex] > mylist[j]):
                minValueIndex = j
                
        temp = mylist[i]
        mylist[i] = mylist[minValueIndex]
        mylist[minValueIndex] = temp
    
    return mylist
            
        
        
mylist = [90, 350, 60, 70, 27, 3, 8]
selectionSort(mylist)
print(mylist)
    


# In[ ]:





# In[ ]:




