# Coding interview preparation notes


Divide it into 4 parts
1. SQL
2. Coding - Data Structure 
3. Coding - Algorithms
4. Complexity calculations


Collect CheatSheets
> https://github.com/vivek-bombatkar/MyLearningNotes/blob/master/coding_interview/CrackingTheCodingInterview.pdf

> https://github.com/vivek-bombatkar/MyLearningNotes/blob/master/coding_interview/PythonCheatSheet.pdf

> https://github.com/vivek-bombatkar/MyLearningNotes/blob/master/coding_interview/Python_2_7.pdf

> https://github.com/vivek-bombatkar/MyLearningNotes/blob/master/coding_interview/big-o-cheat-sheet-poster.png

> https://github.com/vivek-bombatkar/MyLearningNotes/blob/master/coding_interview/main-qimg-420e994dba8284996618d7922be544d2.png

> https://github.com/vivek-bombatkar/MyLearningNotes/blob/master/coding_interview/mementopython3-english.pdf

> https://github.com/vivek-bombatkar/MyLearningNotes/blob/master/coding_interview/python_cheat_sheet.pdf


Random link
> https://www.qt.io/qt-for-application-development/

> https://www.geeksforgeeks.org/

> http://highscalability.com/

> https://projecteuler.net/index.php

> https://www.codechef.com/

> https://www.careercup.com/page


# 1. SQL
Practice SQL Interview questions and Answers

> http://sqlzoo.net/   
> https://www.hackerrank.com/   
> https://leetcode.com/problemset/database/   
> https://www.tutorialspoint.com/dwh/dwh_schemas.htm  

- SQL Good reads   
> https://www.geeksforgeeks.org/sql-correlated-subqueries/    
> 

- 'windowing' function
> https://cwiki.apache.org/confluence/display/Hive/LanguageManual+WindowingAndAnalytics  
> https://blog.matters.tech/sql-window-functions-basics-e9a9fa17ce7e  
- select > partition > order  
- use windowing over (self join + group by)  
- windowing functions are a select post-processing toolset  
- iterate over the result of a select to compute values based on a wider view than just one row.  
- At its core, a window function calculates a return value for every input row of a table based on a group of rows, called the Frame  
- Rank vs DenseRank  : 
- three kinds of window functions: 1. ranking functions 2. analytic functions 3. aggregate functions  
```SQL
OVER (PARTITION BY ... ORDER BY ...)
```
- Window functions are also called over functions due to how they are applied using over operator.  
- Lead & Lag : to traverse up and down in the rows  
- 

- 2 Nth highest salary  
	- corelated subquery  
		-  subquery depends upon the main query  
		- execute for every row returned by the main query.  
		```
		SELECT name, salary 
		FROM #Employee e1
		WHERE N-1 = (SELECT COUNT(DISTINCT salary) FROM #Employee e2
		WHERE e2.salary > e1.salary)
		```
	- windowing  
		- 
		```
		WITH CTE AS
		(
		SELECT Name, Salary, DENSE_RANK() OVER (Salary ORDER BY SALARY DESC) AS Ranks
		FROM Employees
		)
		SELECT * FROM CTE WHERE Ranks=2
		```
- 3 running total
	- self join
		-   we take the sum of sales in the second table over every row that has a date less than or equal to the date coming from the first table.  
		```
		select 
		    a.date,
		    sum(b.sales) as cumulative_sales
		from sales_table a 
		join sales_table b on a.date >= b.date
		group by a.date
		order by a.date;
		```
	- windowing functions
		- order by date rows unbounded preceding limits the sum function to only sales before the date of the current row.   
		```
		select
	    	date,
	    	sum(sales) over (order by date rows unbounded preceding) as cumulative_sales
		from sales_table;
		```
		
		

# 2. Data Structure
> https://www.tutorialspoint.com/python/python_data_structure.htm
> Video tutorial Py Datastructure :   
https://www.youtube.com/watch?v=4f225AUHGAY&list=PLib7LoYR5PuDxi8TxxGKxMgf8b-jtoS3i&index=7     
https://www.youtube.com/channel/UCFxcvyt2Ucq5IL0_1Njzqlg/playlists?view=50&sort=dd&shelf_id=4  

- Py Native Data Structures  
1. List  
2. Tuples  
3. Dict  
4. Sets  

- Advance DS  
1. Link List
2. Trees  
3. Graphs  
4. Stack  
5. Queue  
6. 



- BT vs Binary Search Trees  




- Random HandsOn  

```python 
def sorting(_list: [])-> []:
    return _list.sort()


old_list = [30,20,10,50]
#sets and tuples has no attribute 'sort'
new_list = sorting(old_list)
print(old_list) # [10, 20, 30, 50]
print(new_list) # None
```  

```  
i=[[1,2,4,7],[21,22,24,'a']]
print(id(i))
j=i
i.pop()
print (id(i))
print (id(j))

print("######")
i=10
print (id(i))
j=i
i=i+1
print (id(i))
print (id(j))
```

```
def changeValue(thisObject,thisValue):
    thisObject += thisValue

int_n = [10,20]
print (id(int_n))
changeValue(int_n,[20])
print (int_n)
print (id(int_n))

int_n = 10
print (id(int_n))
changeValue(int_n,30)
print (int_n)
print (id(int_n))
```

```
class Node:
    def __init__(self,val):
      self.val = val
      self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

print node1
```

```
dictOne = dict(one=1,two=2)
dictTwo = dict(zip(['one','two'],[10,20]))
print (dictTwo['one'])
```

> https://www.programiz.com/python-programming/set
A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).	
setFirst = set([9,2,1,2,4,5,0,-1,35.5,35.3])
print sorted(setFirst)


tupFirst = tuple(['dasfsdf',10])
print tupFirst

> https://www.tutorialspoint.com/python/python_hash_table.htm
In Python, the Dictionary data types represent the implementation of hash tables. The Keys in the dictionary satisfy the following requirements.

The keys of the dictionary are hashable i.e. the are generated by hashing function which generates unique result for each unique value supplied to the hash function.
The order of data elements in a dictionary is not fixed.

- link list  
> https://www.tutorialspoint.com/python/python_linked_lists.htm
```
class Node:
    def __init__(self,thisValue = None):
        self.value=thisValue
        self.nextNode=None
class LinkList:
    def __init__(self):
        self.headValue=None
    def traverseList(self):
        thisNode=self.headValue
        while thisNode is not None:
            print thisNode.value
            thisNode=thisNode.nextNode
    def addBegining(self,newData):
        newNode=Node(newData)
        newNode.nextNode=self.headValue
        self.headValue=newNode
    def addEnd(self,newData):
        newNode=Node(newData)
        if self.headValue is None:
            self.headValue=newNode
        else:
            lastNode=self.headValue
            while(lastNode.nextNode):
                lastNode=lastNode.nextNode
            lastNode.nextNode=newNode
    def addInbetween(self,middleNode,newData):
        newNode=Node(newData)
        newNode.nextNode=middleNode.nextNode
        middleNode.nextNode=newNode
    def removeNode(self,removeKey):
        headNode=self.headValue
        if headNode is not None:
            if headNode.value==removeKey:
                self.headValue=headNode.nextNode
                headNode=None
            else:
                while(headNode is not None):
                    if headNode.value==removeKey:
                        break
                    prevNode=headNode
                    headNode=headNode.nextNode
                if (headNode==None):
                    return
                prevNode.nextNode=headNode.nextNode
                headNode=None

linkList=LinkList()
linkList.headValue=Node("genesis")
nodeOne=Node("one")
nodeTwo=Node("two")
linkList.headValue.nextNode=nodeOne
nodeOne.nextNode=nodeTwo
linkList.addBegining("theNewNode")
linkList.addEnd("LastNode")
linkList.addInbetween(linkList.headValue.nextNode,"MiddleNode")
linkList.removeNode("two")
linkList.traverseList()
```

- stack  
>

```
class Stack:
    def __init__(self):
        self.stack=[]
    def pushStack(self,thisValue):
        self.stack.append(thisValue)
        return True
    def peek(self):
        return self.stack[0]
    def popStack(self):
        if(len(self.stack)>=1):
            self.stack.pop()
        return
myStack=Stack()
myStack.pushStack("one")
myStack.pushStack("two")
print myStack.peek()
myStack.popStack()
myStack.popStack()
print myStack.peek()
```

- queue and collections.deque  

```
class Queue:
    def __init__(self):
        self.queue=list()
    def addQueue(self,thisValue):
        self.queue.insert(0,thisValue)
        return
    def removeQueue(self):
        self.queue.pop()
        return
    def getSize(self):
        return len(self.queue)
myQueue=Queue()
myQueue.addQueue("one")
myQueue.addQueue("two")
myQueue.addQueue("three")
myQueue.removeQueue()
print myQueue.getSize()
for element in myQueue.queue:
    print element
	
from collections import deque

myDqueue=deque(["one","two","three"])
print myDqueue
myDqueue.pop()
print myDqueue
myDqueue.append("four")
print myDqueue
myDqueue.appendleft("zero")
print myDqueue
```

- Binary Tree  

```
class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    def insert(self,data):
        if self.data:
            if self.data < data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def findNode(self,data):
        if self.data>data:
            if self.left is None:
                return ("Not found!")
            return self.left.findNode(data)
        elif self.data<data:
            if self.right is None:
                return ("Not found")
            return self.right.findNode(data)
        else:
            print("Node found")
root=Node(0)
root.insert(10)
root.insert(20)
root.insert(50)
root.insert(5)
root.printTree()
print(root.findNode(21))
```

-  Binary Search using iterator  
```
class BinarySearch:
    def findValue(self,list,value):
        last_pos=len(list)-1
        start_pos=0
        while start_pos < last_pos:
            middle_value = (last_pos+start_pos)//2
            if list[middle_value]==value:
                return middle_value
            if list[middle_value] < value:
                start_pos=middle_value+1
            else:
                last_pos=middle_value-1
        if start_pos > last_pos:
            return None

array=(10,20,30,40,50,60,70,80)
BS=BinarySearch()
print(BS.findValue(array,40))
```

```
def reverse_numbers(int_this):
    this_reverse=''
    str_this=str(int_this)
    for i in range(len(str_this)-1,-1,-1):
        this_reverse += str_this[i]
    return this_reverse

print(reverse_numbers(123456))
```

```
def checkIfSubstring(str_this,substr_this):
    for str in str_this.split(" "):
        if str == substr_this:
            return "True"
    return "False"

print(checkIfSubstring("this is my code","code"))
```

```         
def maxOfList(lst_this):
    maxElement=0
    for element in lst_this:
        if maxElement < element:
            maxElement=element
    return maxElement

print(maxOfList([1,4,2,5,7,2,1,7]))
```

```
def medianOfList(a_list):
    sumElements=0
    for element in a_list:
        sumElements+=element
    return (sumElements / len(a_list)-1)

print(medianOfList([1,2,3,4,5,6,7,8,9]))
```


-  Binary Search using recursion  
```

```


- Solved problems  
 Two Sum : https://www.youtube.com/watch?v=gCin6Qz-eJQ&list=PL5tcWHG-UPH1YSW2RraQg2L2p5hQTIpNL&index=3

```


class ListList():
    def __init__(self):
        self.nodes = []

    def add(self,node):
        return self.nodes.append(node)
    
def look_and_say(sequence:[])->[]:
    res = []
    for i in range(len(sequence)):
        if i>0 & sequence[i] == sequence[i-1]:
            res.pop()
            res.pop()
            res.append(2)
            res.append(sequence[i])
        else:
            res.append(1)
            res.append(sequence[i])
        # res.append(sequence[i])
    return res

def is_palindrome_1(given_string: str)-> bool:
    tmp = given_string.replace(" ","").lower()
    print(tmp)
    if tmp.strip() == tmp[::-1].strip() :
        return True
    return False

def is_palindrome_2(given_str: str)->bool:
    tmp = given_str.replace(" ","").lower()
    i= 0
    j = len(tmp) -1
    while i < j:
        if tmp[i] != tmp[j]:
            return False
        i += 1
        j -= 1
    return True

def is_anagram(str_1, str_2):
    tmp1 = ([s for s in str_1.replace(" ","")])
    tmp2 = ([s for s in str_2.replace(" ", "")])
    # if sorted(tmp1) !=  sorted(tmp2) :
    #     return False
    for s in tmp1:
        if s in tmp2:
            tmp2.remove(s)
        else:
            return False
    return True

def is_all_qunique(given_str):
    processed_elem = []
    for s in given_str:
        if s in processed_elem:
            return False
        else:
            processed_elem.append(s)
    return True
def is_all_qunique_2(given_str):
    for i in range(len(given_str)):
        if given_str[i] in given_str[i+1:len(given_str)]:
            return False
    return True

def what_is_sets(given_str: str):
    return set(given_str)

def recur_first_upper(given_str,index):
    if (len(given_str) -1 == index):
        return "NON"
    elif given_str[index].isupper():
        return given_str[index]
    print(given_str[index])
    return  recur_first_upper(given_str,index+1)

def recr_len_str(given_str):
    print(given_str)
    if given_str == "":
        return 0
    return 1 + recr_len_str(given_str[1:])

def recr_product(num_1, num_2):
    print("Called...")
    # print(f'{num_1}, {num_2}')
    if num_1 == 1:
        return num_2
    print(num_2 + recr_product(num_1 -1 ,num_2))
    return num_2 + recr_product(num_1 -1 ,num_2)

def recr_linear_search(given_list,search_element):
    if given_list == []:
        return False
    if search_element == given_list[0]:
        return True
    return recr_linear_search(given_list[1:],search_element)

def itr_binary_search(given_list, serach_elemnt):
    subset_list = given_list
    center = (len(given_list) // 2)
    while center >= 0:
        print(center)
        if serach_elemnt > center:
            subset_list = subset_list[center:]
        else:
            subset_list = subset_list[:center]
        center = len(subset_list) // 2
        if subset_list[center] == serach_elemnt:
            return True
        print(subset_list)
    return False

def recur_binary_search(given_list,search_element):
    list_lenght = len(given_list) -1
    list_center = (list_lenght // 2)
    if search_element in [given_list[list_center], given_list[0],given_list[list_lenght]]:
        return True
    elif search_element > given_list[list_lenght] or search_element < given_list[0]:
        return False

    if search_element > list_center:
        return recur_binary_search(given_list[list_center + 1:],search_element)
    else:
        return recur_binary_search(given_list[:list_center],search_element)

    # if search_element

def shift_list(given_list):
    print(given_list)
    result =[]
    if len(given_list) <= 1:
        return list
    else:
        last = given_list[-1]
        result += [last]
        for i in given_list[:-1]:
            result += [i]


    return result

def recr_get_fibonachi(n):
    febi = [0,1]
    while i in range(len(febi)):
        if n in febi:
            return febi.index(n)
        febi.append(febi[i]+febi[+1])
    return 0
    
    
```

 
# 3. Algorithms
> https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889   
> https://leetcode.com/problemset/algorithms/    

- IMP search Algos  
1. Bubble  - swap firt pair of elements, swap smaller to first position   
```
#O(n^2)
def bubble_sort(_list: []) -> []:
    for i in range(len(_list)):
        for j in range(i+1,len(_list)):
            if _list[j] < _list[i]:
                tmp = _list[i]
                _list[i] = _list[j]
                _list[j] = tmp
    return _list
```

2. Selection - linear scan, bring first smaller element to first, then look for second smallest   
```python
#O(n^2)
def selection_sort(_list:[]) -> []:
    for i in range(len(_list)):
        min_index = i
        for j in range(i+1, len(_list)):
            if _list[i] > _list[j]:
                min_index = j
        _list[i],_list[min_index] = _list[min_index], _list[i]
    return _list
```
3. Quick  - pick random element, move all smaller to first half and bigger to right half, then repeate for each half  
4. Merge  - sort each pair first, then sort four by merging pair, then sort 8...  
5. Bucket  - partition array into bucket and sort bucket individually    
6. Insertion sort - remove one element from array and add to another sorted array at right position   
```python
def insertion_sort(_list:[]) -> []:
    for i in range(len(_list)):
        current_element = _list[i]
        current_position = i
        while current_position > 0 and _list[current_position - 1] > current_element:
            _list[current_position] = _list[current_position - 1]
            current_position = current_position - 1
        _list[current_position] = current_element
    return _list
```    


# 4. Complexity  
- Big O notation    
> https://www.youtube.com/playlist?list=PL2_aWCzGMAwI9HK8YPVBjElbLbI3ufctn  
```
1 for each assignment / calculation 
n for loop

ignore constants
o(n) - loop
o(n) + o(m) - multiple loops
o(n^2) - inner loop
o(log n) - loop reduce factor
```

# Extra notes:   
- Data Warehouse  
> http://cs.ulb.ac.be/public/_media/teaching/infoh415/dwnotes.pdf  
> 
