You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.

 

Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].


SOLUTION:

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        def flatten(nested_list):
            res = []
            for e in nested_list:
                if e.isInteger():
                    res.append(e.getInteger())
                else:
                    res.extend(flatten(e.getList()))
            return res
        
        self.flat_list = flatten(nestedList)
        
    def next(self) -> int:
        return self.flat_list.pop(0)
    
    def hasNext(self) -> bool:
         return len(self.flat_list)>0