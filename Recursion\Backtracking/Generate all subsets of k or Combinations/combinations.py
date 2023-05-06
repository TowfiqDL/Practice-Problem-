##Taking the subset of size k from all subsets of n. Time complexity is O(k*2^N) and Space Complexity is O(k*2^N) if we store all the data in an array. 

def combinations(n, k): 
  def helper(indx, currSet, subSets):
    ##Base Case 
    if len(currSet) == k: 
      subSets.append(currSetcopy())
      return 
    if indx > n: 
      return
    
    currSet.append(indx)
    helper(indx+1, currSet, subSets)
    currSet.pop()
    
    helper(indx+1, currSet, subSets)
  
  
  currSet, subSets = [], []
  helper(1, currSet, subSets) 
  
  return subSets


##Building a recursive tree with time complexity O(nCk). 

def combinations_eff(n, k):
    def helper(indx, currSet, subSets):
        if len(currSet) == k:
            subSets.append(currSet.copy())
            return
        if indx > n:
            return
        for j in range(indx, n+1):
            currSet.append(j)
            helper(j+1, currSet, subSets)
            currSet.pop()



    currSet, subSets = [], []
    helper(1, currSet, subSets)
    return subSets
  
  
  
